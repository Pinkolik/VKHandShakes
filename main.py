import VKHandShakes


def main():
    vk_hand_shakes = VKHandShakes.VKHandShakes(7941450, 125435052)
    vk_hand_shakes.calculate_route()
    vk_hand_shakes.print_routes()
    return 0


if __name__ == '__main__':
    main()
