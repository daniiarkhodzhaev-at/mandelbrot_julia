#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

const int NUM_STEPS = 1024;

static int col1[] = {156,  38, 177};
static int col2[] = { 64,  82, 182};
static int col3[] = {  0, 169, 246};

int _set_color(int r1, int g1, int b1,
              int r2, int g2, int b2,
              int r3, int g3, int b3) {
    col1[0] = r1;
    col1[1] = g1;
    col1[2] = b1;
    col2[0] = r2;
    col2[1] = g2;
    col2[2] = b2;
    col3[0] = r3;
    col3[1] = g3;
    col3[2] = b3;

    return 0;
}

static void *__vec3(int r, int g, int b) {
    int *ans = malloc(sizeof(int) * 3);
    *ans = r;
    *(ans+1) = g;
    *(ans+2) = b;
    return ans;
}

static void *__mix(double a1, double a2, double a3) {
    return __vec3(col1[0] * a1 + col2[0] * a2 + col3[0] * a3,
                col1[1] * a1 + col2[1] * a2 + col3[1] * a3,
                col1[2] * a1 + col2[2] * a2 + col3[2] * a3);
}

static void *__constructColor(int iter) {
    if (iter == NUM_STEPS) {
        return __vec3(0, 0, 0);
    }

    double i = iter % 20 / 20.0;
    int cel = iter / 20 % 3;

    if (cel == 0) {
        return __mix(i, 1 - i, 0);
    }
    if (cel == 1) {
        return __mix(1 - i, 0, i);
    }
    if (cel == 2) {
        return __mix(0, i, 1 - i);
    }
    return __vec3(0, 0, 0);
}

void *_calc_man(int width, int height,
        double mx, double my, double dmx, double dmy) {

    int *ans = malloc(sizeof(int)*width*height*3);
    double x, y, x0, y0, tmp;
    int *col;
    int cnt;
    for (int i = 0; i < width; ++i) {
        for (int j = 0; j < height; ++j) {
            x0 = 0;
            y0 = 0;
            x = mx - dmx / 2 + dmx * i / width;
            y = my - dmy / 2 + dmy * j / height;
            cnt = 0;
            while (x0 * x0 + y0 * y0 < 4 && cnt < NUM_STEPS) {
                tmp = x0 * x0 - y0 * y0 + x;
                y0 = 2 * x0 * y0 + y;
                x0 = tmp;
                cnt++;
            }
            col = (int *)__constructColor(cnt);
            *(ans + height * 3 * i + j * 3 + 0) = col[0];
            *(ans + height * 3 * i + j * 3 + 1) = col[1];
            *(ans + height * 3 * i + j * 3 + 2) = col[2];
            free(col);
        }
    }
    return ans;
}

void *_calc_jul(int width, int height,
        double cx, double cy,
        double jx, double jy, double djx, double djy) {

    int *ans = malloc(sizeof(int)*width*height*3);
    double x0, y0, tmp;
    int *col;
    int cnt;
    for (int i = 0; i < width; ++i) {
        for (int j = 0; j < height; ++j) {
            x0 = jx - djx / 2 + djx * i / width;
            y0 = jy - djy / 2 + djy * j / height;
            cnt = 0;
            while (x0 * x0 + y0 * y0 < 4 && cnt < NUM_STEPS) {
                tmp = x0 * x0 - y0 * y0 + cx;
                y0 = 2 * x0 * y0 + cy;
                x0 = tmp;
                cnt++;
            }
            col = (int *)__constructColor(cnt);
            *(ans + height * 3 * i + j * 3 + 0) = col[0];
            *(ans + height * 3 * i + j * 3 + 1) = col[1];
            *(ans + height * 3 * i + j * 3 + 2) = col[2];
            free(col);
        }
    }
    return ans;
}

void _free(void * ptr) {
    free(ptr);
}
