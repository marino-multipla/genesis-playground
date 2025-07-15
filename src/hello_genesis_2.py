import genesis as gs

gs.init(
    seed                = None,
    precision           = '32',
    debug               = False,
    eps                 = 1e-12,
    logging_level       = None,
    backend             = gs.gpu,
    theme               = 'dark',
    logger_verbose_time = False
)

scene = gs.Scene(
    sim_options=gs.options.SimOptions(
        dt=0.01,
        gravity=(0, 0, -10.0),
    ),
    show_viewer=True,
    viewer_options=gs.options.ViewerOptions(
        camera_pos=(3.5, 0.0, 2.5),
        camera_lookat=(0.0, 0.0, 0.5),
        camera_fov=40,
    ),
)

plane = scene.add_entity(gs.morphs.Plane())

franka = scene.add_entity(
    gs.morphs.MJCF(
        file  = 'xml/franka_emika_panda/panda.xml',
        pos   = (0, 0, 0),
        euler = (0, 0, 90), # we follow scipy's extrinsic x-y-z rotation convention, in degrees,
        # quat  = (1.0, 0.0, 0.0, 0.0), # we use w-x-y-z convention for quaternions,
        scale = 1.0,
    ),
)

scene.build()
for i in range(1000):
    scene.step()

