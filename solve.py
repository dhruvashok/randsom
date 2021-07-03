#!/usr/bin/env python3
import pwn
import time
import random

def gen_rand(seed):
    random.seed(seed)
    return [random.randint(1, 255) for _ in range(32)]

def solve():
    # r = pwn.process("./randsom.py")
    r = pwn.remote("4.tcp.ngrok.io", 19031)
    r.recv()
    r.sendline('Y') # ask for an encrypted flag
    flag_enc = r.recv().decode().split("\n")[0].split(": ")[1] # get the encrypted flag
    current_time = int(time.time()) # get the current time, since it's used as our seed
    pwn.log.success(f'Got encrypted flag: {flag_enc}')
    pwn.log.success(f'Got seed: {current_time}')
    nums = gen_rand(current_time) # seed the RNG with the current time and generate the same set of 32 numbers
    flag_enc = bytes.fromhex(flag_enc) # convert the encrypted flag hex to bytes
    flag = bytes((x ^ y) % 256 for x, y in zip(flag_enc, nums)) # reverse the XOR to decrypt the flag
    pwn.log.success(f'FLAG: {flag.decode()}')
    r.close()

if __name__ == '__main__':
    solve()
