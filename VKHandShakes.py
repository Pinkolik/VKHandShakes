import requests
import threading


class VKHandShakes:
    service_token = '9f80a4009f80a4009f80a400e19fd7009c99f809f80a400c5fc0f1a903421384f8fad84'
    friends_get_url = 'https://api.vk.com/method/friends.get'

    def __init__(self, source_id: int, destination_id: int, max_depth: int = 5):
        self.source_id = source_id
        self.destination_id = destination_id
        self.max_depth = max_depth
        self.routes = []

    def calculate_route(self):
        routes = [[self.source_id]]
        finish = False
        for i in range(0, self.max_depth):
            routes = self.get_next_level_friends(routes)
            print('Friends at level', i, len(routes))
            for route in routes:
                last_user_id = route[-1]
                if last_user_id == self.destination_id:
                    self.routes.append(route)
                    finish = True
            if finish:
                break

    def get_next_level_friends(self, routes):
        result_routes = []
        thread_pool = []
        for route in routes:
            last_user_id = route[-1]
            thread = threading.Thread(target=self.add_route_to_result_routes, args=(last_user_id, result_routes, route))
            thread_pool.append(thread)
            thread.start()
        for thread in thread_pool:
            thread.join()
        return result_routes

    def add_route_to_result_routes(self, last_user_id, result_routes, route):
        friends_ids = self.get_friends_user_ids(last_user_id)
        if len(friends_ids) > 0:
            for user_id in friends_ids:
                if user_id not in route:
                    new_route = list(route)
                    new_route.append(user_id)
                    result_routes.append(new_route)

    @staticmethod
    def get_friends_user_ids(user_id: int) -> list:
        payload = {'user_id': user_id, 'v': 5.95, 'access_token': VKHandShakes.service_token}
        reply = requests.get(VKHandShakes.friends_get_url, params=payload).json()
        if 'response' in reply:
            return reply['response']['items']
        else:
            # print(reply['error'])
            return []

    def print_routes(self):
        for route in self.routes:
            print(route)
