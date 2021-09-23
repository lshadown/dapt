for (int w0 = floord(-82 * n + 369, 3503) - 1; w0 < floord(n, 113); w0 += 1) {
  #pragma omp parallel for
  for (int h0 = max(-((n + 28) / 31), w0 - (n + 113) / 113 + 1); h0 <= min(-1, w0 + floord(31 * w0 - 24, 82) + 2); h0 += 1) {
    for (int i0 = max(max(-n + 2, -113 * w0 + 113 * h0 - 110), 31 * h0); i0 <= 31 * h0 + 30; i0 += 1) {
      for (int i1 = max(113 * w0 - 113 * h0, -i0 + 2); i1 <= min(n, 113 * w0 - 113 * h0 + 112); i1 += 1) {
        for (int i2 = -i0 + 1; i2 < i1; i2 += 1) {
          c[-i0][i1] = MIN(c[-i0][i1], (w[-i0][i1] + c[-i0][i2]) + c[i2][i1]);
        }
      }
    }
  }
}