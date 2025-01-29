class Fluid {
    int size;
    float dt;
    float diff;
    float visc;

    float[] s;
    float[] density;

    float[] Vx;
    float[] Vy;

    float[] Vx0;
    float[] Vy0;

    Fluid(float dt, float diffusion, float viscosity) {
        int N = size;

        this.size = N;
        this.dt = dt;
        this.diff = diffusion;
        this.visc = viscosity;

        this.s = new float[N * N];
        this.density = new float[N * N];

        this.Vx = new float[N * N];
        this.Vy = new float[N * N];

        this.Vx0 = new float[N * N];
        this.Vy0 = new float[N * N];
    }
};