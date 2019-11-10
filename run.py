from flask import Flask, request
import json
from configs.app import app
from configs.db import db
from models.plan import Plan
import pdb


@app.route('/')
def home():
    # pdb.set_trace()
    return "Hello word!"

# Route to find a plan
@app.route('/plan/<string:plan_id>', methods=['GET'])
def get_plan(plan_id):
    plan = Plan.query.get(plan_id)
    return plan.dictionary

# Get all plans
@app.route('/plans', methods=['GET'])
def get_plans():
    plans = Plan.query.all()
    response = []
    for plan in plans:
        response.append(plan.dictionary)
    return json.dumps(response)


@app.route('/plan', methods=['POST'])
def add_plan():
    # obj: is a dictionary
    obj = json.loads(request.data) 
    plan_object = Plan(
        title=obj['title'], 
        description=obj['description'], 
        finished=obj['finished'], 
        priority=obj['priority'])

    db.session.add(plan_object)
    db.session.commit()
    return "Add successful!"

@app.route('/plan/<string:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    # 1 config the target from client input
    obj = json.loads(request.data)
    # 2 find the target from the table
    plan = Plan.query.filter_by(id=plan_id)
    # 3 update the target on the database
    plan.update(obj)
    # 4 commit 
    db.session.commit()
    return get_plan(plan_id)

@app.route('/plan/<string:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    plan = Plan.query.filter_by(id=plan_id)
    plan.delete()
    db.session.commit()
    return "Delete successful"



if __name__ == "__main__":
    app.run(port=3000)

    