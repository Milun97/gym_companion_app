from database.models import SessionLocal, Base, engine 
from database.models import CoreBodyPart, SubBodyPart, Exercise


def create_db():
    Base.metadata.create_all(bind=engine)

def wipe_db():
    Base.metadata.drop_all(bind=engine)


db = SessionLocal()

def create_data():

    core_body_parts = [CoreBodyPart(name="Chest", description="Pectoral muscles.", image_url="static/img/chest.jpg"),
                        CoreBodyPart(name="Arms", description="Biceps, triceps, and forearms.", image_url="static/img/arms.jpeg"),
                        CoreBodyPart(name="Legs", description="Quadriceps, hamstrings, and calves.", image_url="static/img/legs.jpg"),
                        CoreBodyPart(name="Abs", description="Abdominal muscles.", image_url="static/img/abs.jpg"),
                        CoreBodyPart(name="Shoulders", description="Deltoid muscles.", image_url="static/img/shoulders.jpg"),
                        CoreBodyPart(name="Back", description="Latissimus dorsi, trapezius, and erector spinae muscles.", image_url="static/img/back.jpg")]
    
    db.add_all(core_body_parts)
    db.commit()



    sub_body_parts = [SubBodyPart(name="Upper Chest",
                                    description="The upper chest, or upper portion of the pectoral muscles, is responsible for shoulder flexion and horizontal adduction.", 
                                    core_body_part_id=core_body_parts[0].id),
                        SubBodyPart(name="Middle Chest", 
                                    description="The middle chest, or middle portion of the pectoral muscles, is responsible for shoulder adduction and transverse flexion.", 
                                    core_body_part_id=core_body_parts[0].id),
                        SubBodyPart(name="Lower Chest", 
                                    description="The lower chest, or lower portion of the pectoral muscles, is responsible for shoulder extension and transverse extension.", 
                                    core_body_part_id=core_body_parts[0].id),
                        SubBodyPart(name="Biceps", 
                                    description="The biceps are a two-headed muscle located in the upper arm, responsible for elbow flexion and forearm supination.", 
                                    core_body_part_id=core_body_parts[1].id),
                        SubBodyPart(name="Triceps", 
                                    description="The triceps are a three-headed muscle located in the upper arm, responsible for elbow extension and forearm adduction.", 
                                    core_body_part_id=core_body_parts[1].id),
                        SubBodyPart(name="Forearms", 
                                    description="The forearms consist of several muscles responsible for wrist, hand, and finger movement, including flexion, extension, and rotation.", 
                                    core_body_part_id=core_body_parts[1].id),
                        SubBodyPart(name="Quads", 
                                    description="The quads, or quadriceps, are a group of four muscles located in the front of the thigh responsible for knee extension and hip flexion.", 
                                    core_body_part_id=core_body_parts[2].id),
                        SubBodyPart(name="Hamstrings", 
                                    description="The hamstrings are a group of muscles located in the back of the thigh responsible for knee flexion and hip extension.", 
                                    core_body_part_id=core_body_parts[2].id),
                        SubBodyPart(name="Calves", 
                                    description="The calves, or gastrocnemius and soleus muscles, are located in the back of the lower leg and responsible for ankle plantar flexion, or pointing the toes downward.", 
                                    core_body_part_id=core_body_parts[2].id),
                        SubBodyPart(name="Upper Abs", 
                                    description="The upper abs, or rectus abdominis, is a paired muscle located in the front of the abdomen responsible for trunk flexion and spinal stability.", 
                                    core_body_part_id=core_body_parts[3].id),
                        SubBodyPart(name="Lower abs", 
                                    description="The lower abs, or transverse abdominis, is a paired muscle located in the front of the abdomen responsible for compressing the abdominal contents and stabilizing the spine.", 
                                    core_body_part_id=core_body_parts[3].id),
                        SubBodyPart(name="Obliques", 
                                    description="The obliques, or external and internal obliques, are paired muscles located on the sides of the abdomen responsible for trunk rotation and lateral flexion.", 
                                    core_body_part_id=core_body_parts[3].id),
                        SubBodyPart(name="Front Delts", 
                                    description="The front delts, or anterior deltoids, are a group of muscles located in the front of the shoulder responsible for shoulder flexion and horizontal adduction.", 
                                    core_body_part_id=core_body_parts[4].id),
                        SubBodyPart(name="Side Delts", 
                                    description="The side delts, or medial deltoids, are a group of muscles located on the lateral aspect of the shoulder responsible for shoulder abduction.", 
                                    core_body_part_id=core_body_parts[4].id),
                        SubBodyPart(name="Rear Delts", 
                                    description="The rear delts, or posterior deltoids, are a group of muscles located in the back of the shoulder responsible for shoulder extension and horizontal abduction.", 
                                    core_body_part_id=core_body_parts[4].id),
                        SubBodyPart(name="Upper Back", 
                                    description="The upper back consists of several muscles responsible for scapular retraction and elevation, including the trapezius and rhomboids.", 
                                    core_body_part_id=core_body_parts[5].id),
                        SubBodyPart(name="Lower Back", 
                                    description="The lower back consists of several muscles responsible for spinal extension and rotation, including the erector spinae and multifidus.", 
                                    core_body_part_id=core_body_parts[5].id),
                        SubBodyPart(name="Lats", 
                                    description="The lats, or latissimus dorsi, are a large muscle located in the back responsible for shoulder extension, adduction, and internal rotation.", 
                                    core_body_part_id=core_body_parts[5].id)]

    db.add_all(sub_body_parts)
    db.commit()

    exercises = [Exercise(name="Incline Dumbbell Press", 
                            description="Sit on an incline bench with a dumbbell in each hand. Start with the dumbbells at shoulder level, then push them up above your chest until your arms are straight. Lower the dumbbells back down to shoulder level to complete one repetition.", 
                            animation_url="../static/img/dumbbell-incline-press.gif", sub_body_part_id=sub_body_parts[0].id),
                Exercise(name="Incline Bench Press", 
                            description="Lie on a incline bench with a barbell at chest level. Grasp the bar with a shoulder-width grip and lift it off the rack. Lower the bar to your chest, then press it back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/incline-bench-press.gif", sub_body_part_id=sub_body_parts[0].id),
                Exercise(name="Incline Push-Up", 
                            description="Position yourself face down on the ground with your hands on an elevated surface such as a bench or step, shoulder-width apart and your feet on the ground. Keeping your body in a straight line, lower your body toward the ground by bending your elbows. Push your body back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/incline-pushup.gif", sub_body_part_id=sub_body_parts[0].id),
                Exercise(name="Barbell Bench Press", 
                            description="Lie on a flat bench with a barbell at chest level. Grasp the bar with a shoulder-width grip and lift it off the rack. Lower the bar to your chest, then press it back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/bench-press.gif", sub_body_part_id=sub_body_parts[1].id),
                Exercise(name="Cable Crossover",
                            description=" Adjust the cable pulleys to a low position, and select the desired weight. Grasp the handles and stand facing away from the pulleys. Step forward until your arms are fully extended, then pull the handles up and across your body until they meet in front of your chest. Return the handles to the starting position to complete one repetition.", 
                            animation_url="../static/img/cable.gif", sub_body_part_id=sub_body_parts[1].id),
                Exercise(name="Dumbbell Pullover", 
                            description="Lie perpendicular across a flat bench with your shoulders supported and your hips off the bench. Hold a dumbbell with both hands over your chest, then lower the weight back behind your head until your arms are parallel to the ground. Raise the weight back up over your chest to complete one repetition.", 
                            animation_url="../static/img/dumbbell-pullover.gif", sub_body_part_id=sub_body_parts[1].id),
                Exercise(name="Decline Bench Press", 
                            description="Lie on a decline bench with a barbell at chest level. Grasp the bar with a shoulder-width grip and lift it off the rack. Lower the bar to your lower chest, then press it back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/decline-bench-press.gif", sub_body_part_id=sub_body_parts[2].id),
                Exercise(name="Dip",
                            description=" Grasp two parallel bars and lift yourself up so your arms are straight. Lower your body down by bending your elbows, keeping your elbows tucked in at your sides. Push your body back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/dips.gif", sub_body_part_id=sub_body_parts[2].id),
                Exercise(name="Decline Push-Up", 
                            description="Position yourself face down on the ground with your hands on the ground, slightly wider than shoulder-width apart and your feet on a low surface such as a step or bench. Keeping your body in a straight line, lower your body toward the ground by bending your elbows. Push your body back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/decline-push-up.gif", sub_body_part_id=sub_body_parts[2].id),
                Exercise(name="Barbell Curl", 
                            description=" Stand with your feet shoulder-width apart and grasp a barbell with an underhand grip. Keeping your elbows tucked in at your sides, curl the bar up towards your chest. Slowly lower the bar back down to complete one repetition.", 
                            animation_url="../static/img/barbellcurl.gif", sub_body_part_id=sub_body_parts[3].id),
                Exercise(name="Dumbbell Hammer Curl", 
                            description="Stand with your feet shoulder-width apart and hold a dumbbell in each hand with your palms facing inwards. Keeping your elbows tucked in at your sides, curl the dumbbells up towards your shoulders. Slowly lower the dumbbells back down to complete one repetition.", 
                            animation_url="../static/img/hammer-curl.gif", sub_body_part_id=sub_body_parts[3].id),
                Exercise(name="Chin-Up", 
                            description=" Grasp a pull-up bar with an underhand grip, with your hands shoulder-width apart. Hang from the bar with your arms fully extended, then pull your body up towards the bar until your chin is over the bar. Slowly lower your body back down to complete one repetition.", 
                            animation_url="../static/img/chinup.gif", sub_body_part_id=sub_body_parts[3].id),
                Exercise(name="Close-Grip Bench Press", 
                            description="Lie on a flat bench with a barbell at chest level. Grasp the bar with a narrow, shoulder-width grip and lift it off the rack. Lower the bar to your chest, then press it back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/close-grip.gif", sub_body_part_id=sub_body_parts[4].id),
                Exercise(name="Tricep Pushdown", 
                            description=" Stand facing a cable machine with a high cable attachment. Grasp the cable attachment with an overhand grip, and press the cable down towards your thighs until your arms are fully extended. Slowly release the cable back up to complete one repetition.", 
                            animation_url="../static/img/triceps-pushdown.gif", sub_body_part_id=sub_body_parts[4].id),
                Exercise(name="Dumbbell Kickback", 
                            description="Hold a dumbbell in your right hand and place your left hand and left knee on a bench. Keeping your elbow tucked in at your side, extend your right arm behind you until it is fully extended. Slowly lower the weight back down to complete one repetition.", 
                            animation_url="../static/img/triceps-kickbacks.gif", sub_body_part_id=sub_body_parts[4].id),
                Exercise(name="Barbell Wrist Curl", 
                            description="Grasp the barbell with an underhand grip and rest your forearms on your thighs. Slowly curl the bar up toward your wrists, then lower it back down to the starting position to complete one repetition.", 
                            animation_url="../static/img/barbell-wrist-curl-side.gif", sub_body_part_id=sub_body_parts[5].id),
                Exercise(name="Farmer's Walk", 
                            description=" Hold a heavy weight in each hand and walk forward, keeping your arms straight at your sides. Walk for a desired distance or time, then release the weights to complete the exercise.", 
                            animation_url="../static/img/walk.gif", sub_body_part_id=sub_body_parts[5].id),
                Exercise(name="Reverse Curl", 
                            description="Stand with your feet shoulder-width apart and hold a barbell with an overhand grip, hands shoulder-width apart. Keeping your elbows tucked in at your sides, curl the bar up to your chest. Slowly lower the bar back down to the starting position to complete one repetition.", 
                            animation_url="../static/img/reverse.gif", sub_body_part_id=sub_body_parts[5].id),
                Exercise(name="Barbell Squat", 
                            description="Stand with your feet shoulder-width apart and a barbell resting on your upper back. Lower your body down by bending your knees, keeping your back straight. Push your body back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/squat.gif", sub_body_part_id=sub_body_parts[6].id),
                Exercise(name="Leg Press", 
                            description="Sit on a leg press machine with your back against the pad and your feet shoulder-width apart on the platform. Push the platform away from you until your legs are straight, then slowly release the weight back toward you to complete one repetition.", 
                            animation_url="../static/img/legpress.gif", sub_body_part_id=sub_body_parts[6].id),
                Exercise(name="Lunges", 
                            description="Stand with your feet shoulder-width apart and hold a dumbbell in each hand, palms facing in. Take a large step forward with one foot and lower your body down until your front thigh is parallel to the ground. Push your body back up to the starting position to complete one repetition. ", 
                            animation_url="../static/img/lunges.gif", sub_body_part_id=sub_body_parts[6].id),
                Exercise(name="Romanian Deadlift", 
                            description="Stand with your feet shoulder-width apart and hold a barbell with an overhand grip in front of your thighs. Keeping your back straight, hinge at the hips and lower the barbell down your legs until you feel a stretch in your hamstrings.", 
                            animation_url="../static/img/romanian.gif", sub_body_part_id=sub_body_parts[7].id),
                Exercise(name="Leg Curl", 
                            description="Lie face down on a leg curl machine with your ankles hooked underneath the padded lever. Bend your knees to curl the lever up towards your buttocks, then slowly lower it back down to complete one repetition.", 
                            animation_url="../static/img/legcurl.gif", sub_body_part_id=sub_body_parts[7].id),
                Exercise(name="Glute-Ham Raise", 
                            description="Kneel on a glute-ham raise machine with your feet anchored under the padded rollers. Keeping your body straight, lower yourself down towards the ground as far as you can go, then push yourself back up to complete one repetition.", 
                            animation_url="../static/img/gluteham.gif", sub_body_part_id=sub_body_parts[7].id),
                Exercise(name="Standing Calf Raise", 
                            description="Stand on a raised platform or step with your heels hanging off the edge. Slowly lower your heels down as far as you can, then raise them up as high as you can, squeezing your calf muscles at the top of the movement. Lower your heels back down to complete one repetition.", 
                            animation_url="../static/img/calf-raise-standing.gif", sub_body_part_id=sub_body_parts[8].id),
                Exercise(name="Seated Calf Raise", 
                            description="Sit on a calf raise machine with your toes on the platform and your knees bent at a 90-degree angle. Raise the platform up with your toes as high as you can, then slowly lower it back down to complete one repetition.", 
                            animation_url="../static/img/seated_calf.gif", sub_body_part_id=sub_body_parts[8].id),
                Exercise(name="Jump Rope", 
                            description="Stand with your feet shoulder-width apart and hold a jump rope in your hands. Jump up and down, swinging the rope under your feet and jumping over it each time it comes around. This exercise is great for building endurance in your calf muscles.", 
                            animation_url="../static/img/Rope jump gif.gif", sub_body_part_id=sub_body_parts[8].id),
                Exercise(name="Crunches", 
                            description="Lie on your back with your knees bent and your hands behind your head. Lift your shoulders off the ground and crunch your upper body towards your knees, squeezing your abs at the top of the movement. Lower your shoulders back down to complete one repetition.", 
                            animation_url="../static/img/crunch.gif", sub_body_part_id=sub_body_parts[9].id),
                Exercise(name="Sit-Ups", 
                            description="Lie on your back with your knees bent and your hands behind your head. Lift your shoulders off the ground and sit all the way up, keeping your feet anchored to the ground. Lower your upper body back down to complete one repetition.", 
                            animation_url="../static/img/situp.gif", sub_body_part_id=sub_body_parts[9].id),
                Exercise(name="Leg Raises", 
                            description="Lie on your back with your legs straight up in the air and your hands at your sides. Lower your legs down towards the ground as far as you can without letting your lower back arch off the ground, then lift them back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/Leg-raises.gif", sub_body_part_id=sub_body_parts[9].id),
                Exercise(name="Reverse Crunches", 
                            description="Lie on your back with your knees bent and your hands at your sides. Lift your hips off the ground and bring your knees towards your chest, squeezing your lower abs at the top of the movement. Lower your hips back down to complete one repetition.", 
                            animation_url="../static/img/reverse_crunch.gif", sub_body_part_id=sub_body_parts[10].id),
                Exercise(name="Leg Raises", 
                            description=" Lie on your back with your legs straight up in the air and your hands at your sides. Lower your legs down towards the ground as far as you can without letting your lower back arch off the ground, then lift them back up to the starting position to complete one repetition.", 
                            animation_url="../static/img/Leg-raises.gif", sub_body_part_id=sub_body_parts[10].id),
                Exercise(name="Scissor Kicks", 
                            description="Lie on your back with your legs straight up in the air and your hands at your sides. Lower one leg down towards the ground as far as you can while keeping the other leg straight up in the air. Alternate between legs in a scissor-like motion, keeping your abs engaged throughout the movement.", 
                            animation_url="../static/img/scissors.gif", sub_body_part_id=sub_body_parts[10].id),
                Exercise(name="Russian Twists", 
                            description="Sit on the ground with your knees bent and your feet flat on the floor. Lean back slightly and hold a weight or medicine ball with both hands in front of your chest. Twist your torso to one side and touch the weight to the ground next to your hip, then twist to the other side and touch the weight to the ground next to your other hip.", 
                            animation_url="../static/img/russian.gif", sub_body_part_id=sub_body_parts[11].id),
                Exercise(name="Side Plank", 
                            description="Lie on your side with your elbow directly under your shoulder and your legs straight out. Lift your hips off the ground and hold the position for a set amount of time. Repeat on the other side.", 
                            animation_url="../static/img/sideplank.jpg", sub_body_part_id=sub_body_parts[11].id),
                Exercise(name="Bicycle Crunches", 
                            description="Lie on your back with your knees bent and your hands behind your head. Lift your shoulders off the ground and bring one elbow towards the opposite knee while extending the other leg out straight. Alternate between sides in a pedaling motion, keeping your abs engaged throughout the movement.", 
                            animation_url="../static/img/bicycle_crunch.gif", sub_body_part_id=sub_body_parts[11].id),
                Exercise(name="Shoulder Press", 
                            description="Stand or sit with dumbbells or a barbell held at shoulder height. Press the weights straight up over your head until your arms are fully extended, then lower the weights back down to shoulder height to complete one repetition.", 
                            animation_url="../static/img/shoulder_press.gif", sub_body_part_id=sub_body_parts[12].id),
                Exercise(name="Front Raises", 
                            description="Stand with dumbbells at your sides and palms facing your body. Lift the weights straight out in front of you until they are level with your shoulders, then lower them back down to your sides to complete one repetition.", 
                            animation_url="../static/img/Dumbbell-Front-Raise.gif", sub_body_part_id=sub_body_parts[12].id),
                Exercise(name="Arnold Press", 
                            description=" Hold dumbbells in front of your chest with your palms facing your body. Press the weights up and out to the sides until your arms are fully extended, then twist your wrists so that your palms are facing forward at the top of the movement. Lower the weights back down to your chest and twist your wrists back to the starting position to complete one repetition.", 
                            animation_url="../static/img/arnold-dumbbell-press.gif", sub_body_part_id=sub_body_parts[12].id),
                Exercise(name="Lateral Raises", 
                            description="Stand with dumbbells at your sides and palms facing your body. Lift the weights out to the sides until they are level with your shoulders, then lower them back down to your sides to complete one repetition.", 
                            animation_url="../static/img/lateral_raises.gif", sub_body_part_id=sub_body_parts[13].id),
                Exercise(name="Upright Rows", 
                            description="Stand with dumbbells held in front of your thighs, palms facing your body. Pull the weights up towards your chin, keeping your elbows higher than your wrists, then lower the weights back down to your thighs to complete one repetition.", 
                            animation_url="../static/img/upright_row.gif", sub_body_part_id=sub_body_parts[13].id),
                Exercise(name="Front Raises", 
                            description="Stand with dumbbells at your sides and palms facing your body. Lift the weights straight out in front of you until they are level with your shoulders, then lower them back down to your sides to complete one repetition.", 
                            animation_url="../static/img/Dumbbell-Front-Raise.gif", sub_body_part_id=sub_body_parts[13].id),
                Exercise(name="Rear Delt Flyes", 
                            description="Hold dumbbells and bend forward at the waist with your feet hip-width apart. Keeping a slight bend in your elbows, lift the weights out to the sides until your arms are parallel to the ground, then lower them back down to complete one repetition.", 
                            animation_url="../static/img/rear_delt.gif", sub_body_part_id=sub_body_parts[14].id),
                Exercise(name="Face Pulls", 
                            description="Attach a rope to a cable machine at shoulder height. Grab the rope with both hands and step back, keeping your arms straight. Pull the rope towards your face, keeping your elbows high and wide, then slowly release back to the starting position to complete one repetition.", 
                            animation_url="../static/img/face-pull.gif", sub_body_part_id=sub_body_parts[14].id),
                Exercise(name="Bent Over Rear Delt Raises", 
                            description="Hold dumbbells and bend forward at the waist with your feet hip-width apart. Keeping a slight bend in your elbows, lift the weights out to the sides until your arms are parallel to the ground, then lower them back down to complete one repetition.", 
                            animation_url="../static/img/bent_raises.gif", sub_body_part_id=sub_body_parts[14].id),
                Exercise(name="Pull-Ups", 
                            description="Grab onto a pull-up bar with palms facing away from you and hands shoulder-width apart. Pull yourself up until your chin is above the bar, then lower yourself back down to complete one repetition.", 
                            animation_url="../static/img/pullupss.gif", sub_body_part_id=sub_body_parts[15].id),
                Exercise(name="Barbell Rows", 
                            description="Stand with your feet hip-width apart, knees slightly bent, and hold a barbell with an overhand grip. Hinge forward at the hips until your back is parallel to the ground. Pull the bar towards your chest, keeping your elbows close to your body, then lower the bar back down to complete one repetition.", 
                            animation_url="../static/img/barbell_row.gif", sub_body_part_id=sub_body_parts[15].id),
                Exercise(name="Seated Cable Rows", 
                            description=" Sit at a cable machine with your knees slightly bent and feet flat on the floor. Hold the cable handles with both hands, and sit up straight with your arms extended in front of you. Pull the handles back towards your body, squeezing your shoulder blades together, then release back to the starting position to complete one repetition.", 
                            animation_url="../static/img/SeatedCableRow.gif", sub_body_part_id=sub_body_parts[15].id),
                Exercise(name="Deadlifts", 
                            description="Stand with your feet shoulder-width apart, with the barbell on the ground in front of you. Hinge forward at the hips, keeping your back straight, and grip the bar with an overhand or mixed grip. Stand up straight, keeping the bar close to your body, then hinge forward at the hips to lower the bar back down to the ground to complete one repetition.", 
                            animation_url="../static/img/Pause-deadlift.gif", sub_body_part_id=sub_body_parts[16].id),
                Exercise(name="Back Extensions", 
                            description="Lie face down on a back extension machine with your feet secured. Place your hands behind your head, and lift your torso off the pad, squeezing your lower back muscles at the top of the movement. Lower back down to complete one repetition.", 
                            animation_url="../static/img/back_extensionis.gif", sub_body_part_id=sub_body_parts[16].id),
                Exercise(name="Superman", 
                            description="Lie face down on the floor with your arms extended in front of you and your legs straight. Lift your arms, chest, and legs off the floor at the same time, squeezing your lower back muscles at the top of the movement. Lower back down to complete one repetition.", 
                            animation_url="../static/img/superman.gif", sub_body_part_id=sub_body_parts[16].id),
                Exercise(name="Lat Pulldowns", 
                            description="Sit at a lat pulldown machine with your knees under the pads and your feet flat on the floor. Grasp the bar with an overhand grip, wider than shoulder-width apart. Pull the bar down towards your chest, keeping your elbows close to your body, then release back to the starting position to complete one repetition.", 
                            animation_url="../static/img/lat-pulldown-with-pronated-grip.gif", sub_body_part_id=sub_body_parts[17].id),
                Exercise(name="Bent Over Rows", 
                            description="Stand with your feet shoulder-width apart, holding a barbell with an overhand grip. Hinge forward at the hips, keeping your back straight, until your torso is parallel to the ground. Pull the bar towards your chest, keeping your elbows close to your body, then release back to the starting position to complete one repetition.", 
                            animation_url="../static/img/bent_over_rows.gif", sub_body_part_id=sub_body_parts[17].id),
                Exercise(name="Pull-Ups", 
                            description="Grab onto a pull-up bar with palms facing away from you and hands shoulder-width apart. Pull yourself up until your chin is above the bar, then lower yourself back down to complete one repetition.", 
                            animation_url="../static/img/pullupss.gif", sub_body_part_id=sub_body_parts[17].id)]
                

    db.add_all(exercises)
    db.commit()



# example exercises:
# EXERCISES = {
#     "Upper Chest": ["Bench Press", "Incline Dumbbell Press", "Dips"],
#     "Lower Chest": ["Decline Bench Press", "Dumbbell Flyes", "Push-Ups"],
#     "Inner Chest": ["Cable Crossovers", "Pec Deck Flyes", "Dumbbell Pullovers"],
#     "Upper Back": ["Pull-Ups", "Lat Pulldowns", "Seated Rows"],
#     "Lower Back": ["Deadlifts", "Back Extensions", "Good Mornings"],
#     "Lats": ["Barbell Rows", "Dumbbell Rows", "Lat Pulldowns"],
#     "Quads": ["Squats", "Leg Press", "Lunges"],
#     "Hamstrings": ["Romanian Deadlifts", "Leg Curls", "Glute-Ham Raises"],
#     "Calves": ["Calf Raises", "Seated Calf Raises", "Donkey Calf Raises"],
#     "Biceps": ["Barbell Curls", "Dumbbell Curls", "Preacher Curls"],
#     "Triceps": ["Close-Grip Bench Press", "Skull Crushers", "Dips"],
#     "Forearms": ["Wrist Curls", "Reverse Wrist Curls", "Farmer's Walks"],
#     "Front Delts": ["Military Press", "Arnold Press", "Front Raises"],
#     "Side Delts": ["Lateral Raises", "Upright Rows", "Bent-Over Raises"],
#     "Rear Delts": ["Reverse Flyes", "Face Pulls", "Bent-Over Raises"],
#     "Upper Abs": ["Crunches", "Sit-Ups", "Hanging Leg Raises"],
#     "Lower Abs": ["Reverse Crunches", "Leg Raises", "Bicycle Crunches"],
#     "Obliques": ["Russian Twists", "Side Planks", "Windshield Wipers"],
# }