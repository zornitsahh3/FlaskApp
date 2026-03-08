from flask import Flask,jsonify,request
from database import engine
from models import Base

#this creates a table todos
Base.metadata.create_all(bind=engine)

app=Flask(__name__)
# In-memory list of todos (temporary storage)
todos = [
    "Buy milk",
    "Learn Flask",
    "Write code"
]
id=4
@app.route('/',methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})
@app.route('/todos',methods=['GET'])
def all_todos():
    return jsonify(todos)
@app.route('/todos',methods=['POST'])
def new_todos():
    data=request.json #get json sent by a client
    todo=data.get("todo") #extract the todo text
    todos.append(todo) #add to list
    return jsonify({"message": "Todo added","todo":todo}),201
@app.route('/todos/<int:id>', methods=['GET'])
def get_specific_todo(id):
    if id < 0 or id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": todos[id]})
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)