from flask import Blueprint, request

from .data.search_data import USERS



bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def Sortdict(search_dict):
        sorted_dict = {}
        search_order = ['id', 'name', 'age', 'occupation']

        for a in range(len(search_order)):
            for key in search_dict:
                if key == search_order[a]:
                    sorted_dict[key] = search_dict.get(key)
        
        return sorted_dict

def search_users(args):
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

    # Implement search here!
    if args == {}:
        return USERS

    sorted_search = Sortdict(args)
    search_items = []

    for key in sorted_search:
        for dicts in USERS:
            for dictkey in dicts:
                if dicts in search_items:
                    break
                if key == dictkey:
                    if str(sorted_search.get(key)) in str(dicts.get(dictkey)):
                        search_items.append(dicts)


    return search_items


    

    

