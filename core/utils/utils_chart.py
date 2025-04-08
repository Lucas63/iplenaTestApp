import streamlit as st
import matplotlib.pyplot as plt


def draw_front_data(data, container):
    feature_points = data.get("keypoints_2d", {})
    # line_points = data.get("line_points", {})
    fig, ax = plt.subplots()

    # x = [item[0] for item in line_points]
    # y = [item[1] for item in line_points]

    # plt.plot(x, y, linewidth=0.1, color="lightblue")
    with container:
        # Draw dict points
        for key, value in feature_points.items():
            plt.scatter(value[0], value[1], s=40)
            plt.text(value[0] + 5, value[1], s=key)

        # Draw line points
        # plt.plot(x, y)

        plt.gca().invert_yaxis()
        # plt.show()
        st.pyplot(fig)

def draw_side_spine(data, container):
    feature_points = data.get("feature_points", {})
    keypoints_3d_denormalized = data.get("keypoints_3d_denormalized", {})

    feature_points['LEFT_EYE'] = keypoints_3d_denormalized.get("LEFT_EYE", [])[:-1]
    feature_points['RIGHT_HIP'] = keypoints_3d_denormalized.get("RIGHT_HIP", [])[:-1]
    feature_points['LEFT_HIP'] = keypoints_3d_denormalized.get("LEFT_HIP", [])[:-1]


    print(feature_points)
    line_points = data.get("line_points", {})
    fig, ax = plt.subplots()

    x = [item[0] for item in line_points]
    y = [item[1] for item in line_points]


    with container:
        # Draw dict points
        for key, value in feature_points.items():
            plt.scatter(value[0], value[1], s=40)
            plt.text(value[0] + 5, value[1], s=key)

        # Draw line points
        plt.plot(x, y, linewidth=1, color="lightblue")

        plt.gca().invert_yaxis()
        plt.show()
        st.pyplot(fig)