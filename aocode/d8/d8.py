#! /usr/bin/env python3
from copy import deepcopy


def code_runner(mem, backtrack=False):
    PC = 0
    acc = 0
    visited = []
    changed = False
    while True:
        # print(f"PC {PC}\t\tOP:{mem[PC]}")
        if PC >= len(mem):
            print(f"Out of memory bound: {PC}. Bootloader successfully loaded")
            raise IndexError(acc)

        op, arg = mem[PC]

        if PC in (v[0] for v in visited):
            return PC, acc

        elif op == 'acc':
            oryg_pc = PC
            visited.append((oryg_pc, acc))
            acc += int(arg)
            PC += 1

        elif op == 'jmp':
            oryg_pc = PC
            PC += int(arg)
            if not 0 <= PC <= len(mem):
                raise ValueError(
                    f"JMP: PC with wrong value {PC}. From: {oryg_pc}: {mem[oryg_pc]}")

            visited.append((oryg_pc, acc))

        elif op == 'nop':
            oryg_pc = PC
            PC += 1
            if not 0 <= PC <= len(mem):
                raise ValueError(
                    f"NOP: PC with wrong value {PC}. From {oryg_pc}: {mem[oryg_pc]}")

            visited.append((oryg_pc, acc))


if __name__ == '__main__':
    prog = [x.split(' ') for x in open('./input.txt').read().split('\n')]
    print(f"First: {code_runner(prog)[0]}")
    for i in range(len(prog)):
        tmp_prog = deepcopy(prog)
        if tmp_prog[i][0] == 'nop':
            tmp_prog[i][0] = 'jmp'
        elif tmp_prog[i][0] == 'jmp':
            tmp_prog[i][0] = 'nop'
        else:
            continue
        try:
            code_runner(tmp_prog)
        except IndexError as e:
            print(f"Second: {e}")
            break

