def reward_func(params):

    track_width = params["track_width"]
    distance_from_center = params["distance_form_center"]

    distance_from_border = 0.5*track_width - distance_from_center

    if distance_from_border >= 0.1:
        reward=1

    else:
        reward=1e-3

