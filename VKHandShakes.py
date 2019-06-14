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
        routes = [[self.source_id]]
        finish = False
        for i in range(0, self.max_depth):
            routes = self.get_next_level_friends(routes)
            print(len(routes))
            for route in routes:
                last_user_id = route[-1]
                if last_user_id == self.destination_id:
                    self.routes.append(route)
                    finish = True
            if finish:
                break

    def get_next_level_friends(self, routes):
        result_routes = []
        for route in routes:
            last_user_id = route[-1]
            friends_ids = self.get_friends_user_ids(last_user_id)
            for user_id in friends_ids:
                skip = False
                for result_route in result_routes:
                    if user_id in result_route:
                        skip = True
                        break
                if not skip:
                    new_route = route.copy()
                    new_route.append(user_id)
                    result_routes.append(new_route)

        return result_routes

    def get_friends_user_ids(self, user_id: int) -> list:
        try:
            return self.vk.friends.get(user_id=user_id)['items']
        except vk_api.ApiError as api_exception:
            print(api_exception, api_exception.values, sep=' ')
            return []

    def print_routes(self):
        for route in self.routes:
            print(route)
