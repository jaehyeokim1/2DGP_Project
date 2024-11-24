def collide(a, b):
    l_a, bot_a, r_a, top_a = a.get_bb()
    l_b, bot_b, r_b, top_b = b.get_bb()
    return not (l_a > r_b or r_a < l_b or top_a < bot_b or bot_a > top_b)
