import vk_api


class VKHandShakes:
    service_token = '9f80a4009f80a4009f80a400e19fd7009c99f809f80a400c5fc0f1a903421384f8fad84'

    def __init__(self, source_id: str, destination_id: str, max_depth: int = 5):
        self.source_id = source_id
        self.destination_id = destination_id
        vk_session = vk_api.VkApi(token=VKHandShakes.service_token)
        self.vk = vk_session.get_api()

    def calculate_route(self):
        route = [self.source_id]
        depth = 0
        self.calculate_route(route, depth)

    def calculate_route(self, route, depth):
        last_user_id = route[-1]

    def get_friends_user_ids(self, user_id) -> list:
        return self.vk.friends.get(user_id)['items']