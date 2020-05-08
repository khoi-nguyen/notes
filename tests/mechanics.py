from solver.mechanics import motion

tests = [
    (
        motion(t0=0, x0=10, v0=0, X=0, a=-10)[1],
        r"T = - \sqrt{2}, v_{T} = 10 \sqrt{2}\\ "
        + r"T = \sqrt{2}, v_{T} = - 10 \sqrt{2}",
        "1-dimensional motion with constant acceleration",
    ),
    (
        motion(n=2, t0=0, x0=(0, 10), v0=(0, 0), X=(0, 0), a=(0, -10))[1],
        r"T = - \sqrt{2}, v_{T} = \left( 0, \  10 \sqrt{2}\right)\\ "
        + r"T = \sqrt{2}, v_{T} = \left( 0, \  - 10 \sqrt{2}\right)\\ "
        "2-dimensional motion with constant acceleration",
    ),
]
