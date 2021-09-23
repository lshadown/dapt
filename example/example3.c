//dapt code:
#define min(x,y)    ((x) < (y) ? (x) : (y))
#define max(x,y)    ((x) > (y) ? (x) : (y))
#define floord(n,d) (((n)<0) ? -((-(n)+(d)-1)/(d)) : (n)/(d))

for (int w0 = floord(-76 * n + 639, 18437) - 1; w0 < floord(n, 179); w0 += 1) {
  #pragma omp parallel for
  for (int h0 = max(-((n + 100) / 103), w0 - (n + 179) / 179 + 1); h0 <= min(-1, 2 * w0 + floord(27 * w0 - 26, 76) + 4); h0 += 1) {
    for (int i0 = max(max(-n + 2, -179 * w0 + 179 * h0 - 176), 103 * h0); i0 <= 103 * h0 + 102; i0 += 1) {
      for (int i1 = max(179 * w0 - 179 * h0, -i0 + 2); i1 <= min(n, 179 * w0 - 179 * h0 + 178); i1 += 1) {
        for (int i2 = -i0 + 1; i2 < i1; i2 += 1) {
          c[-i0][i1] = MIN(c[-i0][i1], (w[-i0][i1] + c[-i0][i2]) + c[i2][i1]);
        }
      }
    }
  }
}