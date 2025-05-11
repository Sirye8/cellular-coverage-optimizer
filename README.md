# Cellular Network Planning Tool

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)

A Python-based optimization tool for determining the minimum number of cells and optimal sectoring configuration required to cover a geographic area while meeting subscriber traffic demands, using the Erlang B traffic model and frequency reuse principles.

---

## Features

- **Erlang B Traffic Analysis**: 
  - Computes blocking probability using the Erlang B formula for circuit-switched networks.
  - Inverse Erlang B solver (via bisection method) to determine maximum supported traffic per sector.

- **Sectoring Optimization**:
  - Evaluates 60°, 120°, and 180° sectoring configurations to minimize co-channel interference.
  - Validates against industry-standard cluster sizes (N=3,4,7,9,12,13,19,21,28).

- **Scalable Design**:
  - Adapts to variable area sizes, user densities, bandwidth constraints, and QoS requirements (blocking probability, SIR).

---

## Input Parameters

| Parameter | Description | Units | Example Value |
|-----------|-------------|-------|---------------|
| `length` | Geographic length of the area | meters | `10000` |
| `width` | Geographic width of the area | meters | `5000` |
| `user_density` | Subscriber density in the area | users/km² | `1000` |
| `min_sir` | Minimum signal-to-interference ratio (C/I) | dB | `2.167` |
| `user_erlang` | Traffic demand per user | Erlangs | `0.0069` |
| `trunk_bw` | Bandwidth per trunk channel | kHz | `200` |
| `total_bw` | Total system bandwidth | kHz | `20000` |
| `blocking_probability` | Acceptable call blocking probability | - | `0.02` |

### Example Output
```plaintext
Minimum number of cells: 18
Sectoring: 180°
