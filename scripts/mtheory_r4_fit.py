#!/usr/bin/env python3
# mtheory_r4_fit.py
# 依據 11D M-theory R⁴ → 4D 降維流程，計算格點模型
# 在 N = grid_size 時將 β 修正到 (1 + tol) 所需之
# 無量綱 R⁴ 係數 k_phys，並回推實際 lattice 係數 k_lattice。

import argparse
import sympy as sp

def get_args():
    ap = argparse.ArgumentParser(
        description='Solve R⁴ coefficient for given lattice setup')
    ap.add_argument('-N', '--grid-size', type=int, default=32,
                    help='number of lattice points N (default: 32)')
    ap.add_argument('-d', '--delta-lp', type=float, default=10.0,
                    help='grid spacing Δ / ℓ_p  (default: 10)')
    ap.add_argument('-t', '--tol', type=float, default=1e-3,
                    help='relative correction tolerance (default: 1e-3 = 0.1%%)')
    return ap.parse_args()

N_sym, k_sym = sp.symbols('N k')
beta_expr = 4 / N_sym**2 + k_sym / N_sym**3

def solve_k(N_val: int, rel_tol: float) -> float:
    beta_no_k = 4 / N_sym**2
    target    = beta_no_k.subs(N_sym, N_val) * (1 + rel_tol)
    eq        = beta_no_k.subs(N_sym, N_val) + k_sym / N_val**3 - target
    sol_k     = sp.solve(eq, k_sym)
    return float(sol_k[0])

def main():
    args = get_args()
    k_phys    = solve_k(args.grid_size, args.tol)
    scaling   = (1.0 / args.delta_lp)**6
    k_lattice = k_phys * scaling

    print('\n=== M-theory R⁴ coefficient fit ===')
    print(f'N                = {args.grid_size}')
    print(f'Δ / ℓ_p          = {args.delta_lp}')
    print(f'target tolerance = {args.tol:.3e}  ({args.tol*100:.3g} %)')
    print('---------------------------------------------')
    print(f'k_phys (unit ℓ_p) = {k_phys:.6f}')
    # ← 这一行改用科学计数法：
    print(f'k_lattice         = {k_lattice:.6e}')
    print('---------------------------------------------')
    print('Hint:  |k_phys| ≲ 𝒪(1) 表示降維與單位處理一致；')
    print('       |k_lattice| ≪ 1 乃 Δ ≫ ℓ_p 時的正常縮放.')

if __name__ == '__main__':
    main()
