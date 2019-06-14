import VKHandShakes


def main():
    vk_hand_shakes = VKHandShakes.VKHandShakes(49477412, 374493404)
    vk_hand_shakes.calculate_route()
    vk_hand_shakes.print_routes()
    return 0


if __name__ == '__main__':
    main()
