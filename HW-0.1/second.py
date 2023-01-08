def int32_to_ip(int32: int) -> str:

    assert 0 <= int32 <= 4_294_967_295
    output = ''
    for _ in range(4):
        reminder = int32 % 256
        int32 = int32 // 256
        if output:
            output = '.' + output
        output = f'{reminder}' + output
    return output


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
