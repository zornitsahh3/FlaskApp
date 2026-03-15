from flask import Flask,jsonify,request
from database import engine
import models
from sqlalchemy.orm import sessionmaker

#this creates all tables defined in models
models.Base.metadata.create_all(bind=engine)

#creates a session
SessionLocal=sessionmaker(bind=engine)

app=Flask(__name__)

@app.route('/',methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/todos',methods=['GET'])
def all_todos():
    db=SessionLocal()
    todos=db.query(models.Todo).all()

    result=[]
    for todo in todos:
        result.append({
            "id":todo.id,
            "text":todo.text
        })
    db.close()
    return jsonify(result)

@app.route('/todos',methods=['POST'])
def new_todos():
    db=SessionLocal()

    data=request.json
    text=data.get("todo")

    if not text:
        return jsonify({"error": "Todo text is required"}), 400
    
    new_todo=models.Todo(text=text)

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    db.close()

    return jsonify({"message": "Todo added","id":new_todo.id,"text":new_todo.text}),201

@app.route('/todos/<int:id>', methods=['GET', 'PUT'])
def handle_todo(id):
    db = SessionLocal()
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        db.close()
        return jsonify({"error": "Todo not found"}), 404

    if request.method == "GET":
        db.close()
        return jsonify({"id": todo.id, "text": todo.text})

    if request.method == "PUT":
        data = request.json
        text = data.get("todo")
        if not text:
            db.close()
            return jsonify({"error": "Todo text is required"}), 400
        todo.text = text
        db.commit()
        db.refresh(todo)
        db.close()
        return jsonify({"message": "Todo updated", "id": todo.id, "text": todo.text})

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)