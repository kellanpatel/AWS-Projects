from flask import Flask, jsonify, request
import boto3
import os

app = Flask(__name__)

#DynamoDB setup
dynamoDB = boto3.resource('dynamodb', region_name='eu-west-2')
tableName = os.environ.get('DYNAMO_TABLE', 'todos')
table = dynamoDB.Table(tableName)

@app.route('/todos', methods=['GET'])
def get_todos():
    resp = table.scan()
    return jsonify(resp['Items'])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.json
    table.put_item(Item=data)
    return jsonify({'status': 'added'}), 201

@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    table.delete_item(Key={'id': todo_id})
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

