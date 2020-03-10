import Augmentor
p = Augmentor.Pipeline('C:/Users/Daboger/Desktop/train/2')
p.flip_left_right(probability=0.8)
p.rotate(probability=0.3,max_left_rotation=5, max_right_rotation=5)
p.shear(probability=0.5,max_shear_left=5,max_shear_right=5)
p.resize(probability=1,width=512,height=512)
p.sample(3000)