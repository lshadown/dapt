//dapt code:
#define min(x,y)    ((x) < (y) ? (x) : (y))
#define max(x,y)    ((x) > (y) ? (x) : (y))
#define floord(n,d) (((n)<0) ? -((-(n)+(d)-1)/(d)) : (n)/(d))

for (int w0 = floord(-52 * n + 279, 2573) - 1; w0 < floord(n, 83); w0 += 1) {
  #pragma omp parallel for
  for (int h0 = max(-((n + 28) / 31), w0 - (n + 83) / 83 + 1); h0 <= min(-1, 2 * w0 + floord(-21 * w0 + 6, 52) + 2); h0 += 1) {
    for (int i0 = max(max(-n + 2, -83 * w0 + 83 * h0 - 80), 31 * h0); i0 <= 31 * h0 + 30; i0 += 1) {
      for (int i1 = max(83 * w0 - 83 * h0, -i0 + 2); i1 <= min(n, 83 * w0 - 83 * h0 + 82); i1 += 1) {
        for (int i2 = -i0 + 1; i2 < i1; i2 += 1) {
          c[-i0][i1] = MIN(c[-i0][i1], (w[-i0][i1] + c[-i0][i2]) + c[i2][i1]);
        }
      }
    }
  }
}