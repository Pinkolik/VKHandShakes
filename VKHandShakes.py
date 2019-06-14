import vk_api


class VKHandShakes:
    service_token = '9f80a4009f80a4009f80a400e19fd7009c99f809f80a400c5fc0f1a903421384f8fad84'

    def __init__(self, source_id: int, destination_id: int, max_depth: int = 5):
        self.source_id = source_id
        self.destination_id = destination_id
        self.max_depth = max_depth
        self.routes = []
        vk_session = vk_api.VkApi(token=VKHandShakes.service_token)
        self.vk = vk_session.get_api()

    def calculate_route(self):
        route = [self.source_id]
        depth = 0
        self.search_in_friends(route.copy(), depth)

    def search_in_friends(self, route, depth):
        depth += 1
        if depth == self.max_depth:
            return
        last_user_id = route[-1]
        friends_ids = self.get_friends_user_ids(last_user_id)
        if self.destination_id in friends_ids:
            route.append(self.destination_id)
            self.routes.append(route)
            return
        for user_id in friends_ids:
            if user_id not in route:
                new_route = route.copy()
                new_route.append(user_id)
                self.search_in_friends(new_route, depth)

    def get_friends_user_ids(self, user_id: int) -> list:
        try:
            return self.vk.friends.get(user_id=user_id)['items']
        except vk_api.ApiError as api_exception:
            print(api_exception, api_exception.values, sep=' ')

    def print_routes(self):
        for route in self.routes:
            print(route)
