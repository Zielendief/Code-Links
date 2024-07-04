from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    store = []
    uusers = USERS[:]
    """Search users database
    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string
    Returns:
        a list of users that match the search parameters
    """
    ''' 
    # Easy Search 
    for i in USERS:
        if "id" in args:
            if args["id"] == i["id"]:
                store.append(i)
        if "name" in args:
            if args["name"] in i["name"]:
                store.append(i)
        if "age" in args:
            if int(args["age"])+1 == int(i["age"]) or int(args["age"]) == int(i["age"]) or int(args["age"])-1 == int(i["age"]):
                store.append(i)
        if "occupation" in args:
            if args["occupation"] in i["occupation"]:
                store.append(i)
    '''

    # Sorted Search 
    if "id" in args:
        for i in uusers[:]:
            if args["id"] == i["id"]:
                store.append(i)
                uusers.remove(i)
                break
    if "name" in args:
        for i in uusers[:]:
            if args["name"] in i["name"]:
                store.append(i)
                uusers.remove(i)
    if "age" in args:
        for i in uusers[:]:
            if int(args["age"])+1 == int(i["age"]) or int(args["age"]) == int(i["age"]) or int(args["age"])-1 == int(i["age"]):
                store.append(i)
                uusers.remove(i)
    if "occupation" in args:
        for i in uusers[:]:
            if args["occupation"] in i["occupation"]:
                store.append(i)
                uusers.remove(i)
    return store
