def reward_function(params):
    '''
    Reward function for maintaining speed and staying close to the centerline
    '''
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']

    # Initialize reward
    reward = 1e-3  # small default reward

    # Markers for distance from center
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Reward for staying close to centerline
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely off track

    # Bonus for staying on track
    if all_wheels_on_track:
        reward += 0.5

    # Speed reward
    SPEED_THRESHOLD = 1.5  # target speed (adjust as needed)
    if speed >= SPEED_THRESHOLD:
        reward += 0.5  # bonus for maintaining good speed

    # Return the final reward
    return float(reward)
