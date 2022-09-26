import math
def reward_function(params):
    '''
    In @params object:
    {
        "all_wheels_on_track": Boolean,    # flag to indicate if the vehicle is on the track
        "x": float,                        # vehicle's x-coordinate in meters
        "y": float,                        # vehicle's y-coordinate in meters
        "distance_from_center": float,     # distance in meters from the track center 
        "is_left_of_center": Boolean,      # Flag to indicate if the vehicle is on the left side to the track center or not. 
        "heading": float,                  # vehicle's yaw in degrees
        "progress": float,                 # percentage of track completed
        "steps": int,                      # number steps completed
        "speed": float,                    # vehicle's speed in meters per second (m/s)
        "streering_angle": float,          # vehicle's steering angle in degrees
        "track_width": float,              # width of the track
        "waypoints": [[float, float], … ], # list of [x,y] as milestones along the track center
        "closest_waypoints": [int, int]    # indices of the two nearest waypoints.
    }
    '''

    #################
    ### Constants ###
    #################

    MAX_REWARD = 1e2
    MIN_REWARD = 1e-3
    DIRECTION_THRESHOLD = 10.0
    ABS_STEERING_THRESHOLD = 15
    SPEED_THRESHOLD = 1.2

    ########################
    ### Input parameters ###
    ########################
    on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle for calculations
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints'] 
    heading = params['heading']

    # negative exponential penalty
    reward = math.exp(-6 * distance_from_center)

    ########################
    ### Reward functions ###
    ########################

    # def on_track_reward(current_reward, on_track, speed):
    #     if not on_track:
    #         current_reward = MIN_REWARD
    #     elif speed > SPEED_THRESHOLD:
    #         current_reward = MAX_REWARD
    #     else:   
    #         current_reward *= 0.5
    #     return current_reward

    def speed_reward(current_reward, speed):
        if speed >= SPEED_THRESHOLD:
            current_reward = MAX_REWARD
        else:
            current_reward = MIN_REWARD
        return current_reward

    def distance_from_center_reward(current_reward, track_width, distance_from_center):
        # Calculate 3 marks that are farther and father away from the center line
        marker_1 = 0.1 * track_width
        marker_2 = 0.25 * track_width
        marker_3 = 0.5 * track_width

        # Give higher reward if the car is closer to center line and vice versa
        if distance_from_center <= marker_1:
            current_reward *= 1.2
        elif distance_from_center <= marker_2:
            current_reward *= 0.8
        elif distance_from_center <= marker_3:
            current_reward *= 0.4
        else:
            current_reward = MIN_REWARD  # likely crashed/ close to off track

        return current_reward

    def straight_line_reward(current_reward, steering, speed):
        # Positive reward if the car is in a straight line going fast
        if abs(steering) < 0.1 and speed > SPEED_THRESHOLD:
            current_reward *= 1.2
        elif abs(steering) < 0.1 and speed <= SPEED_THRESHOLD:
            current_reward *= 0.8
        return current_reward

    def direction_reward(current_reward, waypoints, closest_waypoints, heading):

        '''
        Calculate the direction of the center line based on the closest waypoints    
        '''

        next_point = waypoints[closest_waypoints[1]]
        prev_point = waypoints[closest_waypoints[0]]

        # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
        direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
        # Convert to degrees
        direction = math.degrees(direction)

        # Cacluate difference between track direction and car heading angle
        direction_diff = abs(direction - heading)

        # Penalize if the difference is too large
        if direction_diff > DIRECTION_THRESHOLD:
            current_reward *= 0.5

        return current_reward

    def steering_reward(current_reward, steering):
        # Penalize reward if the car is steering too much (your action space will matter)
        if abs(steering) > ABS_STEERING_THRESHOLD:
            current_reward *= 0.8
        return current_reward

    # def throttle_reward(current_reward, speed, steering):
    #     # Decrease throttle while steering
    #     if speed > 2.5 - (0.4 * abs(steering)):
    #         current_reward *= 0.8
    #     return current_reward

    ########################
    ### Execute Rewards  ###
    ########################

    # reward = on_track_reward(reward, on_track, speed)
    reward = speed_reward(reward, speed)
    reward = distance_from_center_reward(reward, track_width, distance_from_center)
    reward = straight_line_reward(reward, steering, speed)
    reward = direction_reward(reward, waypoints, closest_waypoints, heading)
    reward = steering_reward(reward, steering)
    # reward = throttle_reward(reward, speed, steering)

    return float(reward)


import math
def reward_function(params):
    
    #################
    ### Constants ###
    #################

    MAX_REWARD = 1
    MIN_REWARD = 1e-3
    DIRECTION_THRESHOLD = 10.0
    ABS_STEERING_THRESHOLD = 15
    SPEED_THRESHOLD = 1.6

    ########################
    ### Input parameters ###
    ########################
    on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle for calculations
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints'] 
    heading = params['heading']

    if not on_track:
        reward = MIN_REWARD
    else:
        reward = MAX_REWARD
        
    if speed >= SPEED_THRESHOLD:
        reward *= 1.5
    else:
        reward *= 0.5

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
            reward *= 1.2
    elif distance_from_center <= marker_2:
            reward *= 0.8
    elif distance_from_center <= marker_3:
            reward *= 0.4
    else:
        reward = MIN_REWARD  # likely crashed/ close to off track

    # Penalize reward if the car is steering too much (your action space will matter)
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # Positive reward if the car is in a straight line going fast
    if abs(steering) < 5 and speed > SPEED_THRESHOLD:
        reward *= 1.2
    elif abs(steering) < 5 and speed <= SPEED_THRESHOLD:
        reward *= 0.8

    '''
    Calculate the direction of the center line based on the closest waypoints    
    '''

    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    # Convert to degrees
    direction = math.degrees(direction)

    # Cacluate difference between track direction and car heading angle
    direction_diff = abs(direction - heading)

    # Penalize if the difference is too large
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5

    return float(reward)


def reward_function(params):

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    SPEED_THRESHOLD = 1.5
    ABS_STEERING_THRESHOLD = 12

    # Calculate 5 marks father away from the center line

    marker_1 = 0.1 * track_width
    marker_2 = 0.20 * track_width
    marker_3 = 0.30 * track_width
    marker_4 = 0.40 * track_width
    marker_5 = 0.5 * track_width

    # Give higher reward if the car is closer to center line 
    if distance_from_center <= marker_1 and all_wheels_on_track:
        track_reward = 3.0
    elif distance_from_center <= marker_2 and all_wheels_on_track:
        track_reward = 2.5
    elif distance_from_center <= marker_3 and all_wheels_on_track:
        track_reward = 1.5
    elif distance_from_center <= marker_4 and all_wheels_on_track:
        track_reward = 1
    elif distance_from_center <= marker_5 and all_wheels_on_track:
        track_reward = 0.5
    else:
        track_reward = 1e-3  # likely crashed/ close to off track  

    if speed <= SPEED_THRESHOLD and speed > 1.2 and all_wheels_on_track:
        speed_reward = 2.5
    elif speed <= 1.2 and speed > 0.9 and all_wheels_on_track:
        speed_reward = 1.5
    elif speed <= 0.9 and speed > 0.7 and all_wheels_on_track:
        speed_reward = 1
    else:
        speed_reward = 1e-3

    reward = track_reward + speed_reward

    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)

def reward_function(params):

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    ABS_STEERING_THRESHOLD = 15

    if speed <= 2.0 and speed > 1.5 and all_wheels_on_track:
        reward = 3.0
    elif speed <= 1.5 and speed > 1.2 and all_wheels_on_track:
        reward = 2.0
    elif speed <= 1.2 and speed > 1.0 and all_wheels_on_track:
        reward = 1.0
    elif speed <= 1.0 and speed > 0.8 and all_wheels_on_track:
        reward = 1e-2
    else:
        reward = 1e-3

    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)