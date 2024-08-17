class GestureRecognition:
    def __init__(self):
        self.previous_gesture = None
        self.current_gesture = None

    def recognize_gesture(self, landmarks):
        hand_open = self.is_open_hand(landmarks)
        number_two = self.is_number_two(landmarks)

        if hand_open and number_two:
            return True
        return False

    def is_open_hand(self, landmarks):
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        return (
            (index_tip.y < thumb_tip.y)
            and (middle_tip.y < thumb_tip.y)
            and (ring_tip.y < thumb_tip.y)
            and (pinky_tip.y < thumb_tip.y)
        )

    def is_number_two(self, landmarks):
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        return (index_tip.y < thumb_tip.y) and (middle_tip.y < index_tip.y)
