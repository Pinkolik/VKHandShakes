import VKHandShakes


def main():
    vk_hand_shakes = VKHandShakes.VKHandShakes(506539848, 173492131)
    vk_hand_shakes.calculate_route()
    vk_hand_shakes.print_routes()
    return 0


if __name__ == '__main__':
    main()
