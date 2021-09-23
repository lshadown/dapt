//dapt code:
#define min(x,y)    ((x) < (y) ? (x) : (y))
#define max(x,y)    ((x) > (y) ? (x) : (y))
#define floord(n,d) (((n)<0) ? -((-(n)+(d)-1)/(d)) : (n)/(d))

for (int w0 = floord(-82 * n + 513, 9983) - 1; w0 < floord(n, 149); w0 += 1) {
  #pragma omp parallel for
  for (int h0 = max(-((n + 64) / 67), w0 - (n + 149) / 149 + 1); h0 <= min(-1, 2 * w0 + floord(-15 * w0 - 34, 82) + 3); h0 += 1) {
    for (int i0 = max(max(-n + 2, -149 * w0 + 149 * h0 - 146), 67 * h0); i0 <= 67 * h0 + 66; i0 += 1) {
      for (int i1 = max(149 * w0 - 149 * h0, -i0 + 2); i1 <= min(n, 149 * w0 - 149 * h0 + 148); i1 += 1) {
        for (int i2 = -i0 + 1; i2 < i1; i2 += 1) {
          c[-i0][i1] = MIN(c[-i0][i1], (w[-i0][i1] + c[-i0][i2]) + c[i2][i1]);
        }
      }
    }
  }
}