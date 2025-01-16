# Personal AI Trainer

## 🏋️ About

This project demonstrates a **Personal AI Trainer** built using **OpenCV**. By leveraging pose estimation, the trainer detects body movements and calculates angles between specific landmarks to evaluate the effectiveness of an exercise. The system focuses on **squat exercises**, providing:

- Real-time feedback on the squat angle accuracy.
- A counter to track the total number of squats completed.

### Key Features:
- Utilizes **three landmarks** for angle calculations: 
  - **Left Hip (p1 = 23)**
  - **Left Knee (p2 = 25)**
  - **Left Ankle (p3 = 27)**
- Calculates squat count and accuracy based on the angles.

---

## 📌 Full-Body Landmarks

The image below shows the **33 distinct full-body landmarks** used for pose tracking:

![Pose Tracking Full-Body Landmarks](https://user-images.githubusercontent.com/37257980/145725762-2c659af2-ec3d-492b-b1b9-0c8e9157d869.png)

---

## 🎥 Pose Detection Demo

Below is a video demonstrating pose detection with all 33 landmarks in action:

https://user-images.githubusercontent.com/37257980/146362573-4487d29a-f6a9-4ec0-b9de-5fa058071f13.mp4

---

## 📊 Output

The system uses the three landmarks (**Left Hip, Left Knee, Left Ankle**) to:

- Calculate the angle during each squat.
- Count the number of squats completed.
- Provide feedback on squat accuracy.

### Demonstration:

**Squat Detection and Counting:**

https://user-images.githubusercontent.com/37257980/145726925-587860e5-49e2-40ab-a258-228bbfead160.mp4

**Additional Example:**

https://user-images.githubusercontent.com/37257980/146348179-a1206ecc-8a84-4a19-9430-31cdefbee79a.mp4

---
