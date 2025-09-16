import random


total_studentd = 63

mentors = (
    '@Daria_Rational',
    '@ReAlist967',
    '@beigecap',
    '@mksgrd ',
    '@bbliketerminal',
    '@trew1237',
    '@Napaste',
    '@sad_bkt',
    '@alex_mack_g',
    '@yarkalm',
    '@med_phisiker',
    '@Daniil_Andreevich_S'
    )

stud_per_mentor = total_studentd // len(mentors)
print('Студентов на ментора', stud_per_mentor)

stud_id = list(range(total_studentd))
print(stud_id)

stud_destrib = {}
for m in mentors:
    stud_for_mentor = random.sample(stud_id, stud_per_mentor)
    stud_destrib[m] = stud_for_mentor
    for v in stud_for_mentor:
        stud_id.remove(v)

# stud_for_mentor = random.sample(stud_id, stud_per_mentor)
# print(stud_for_mentor)
for m in stud_destrib.keys():
    print(m, stud_destrib[m])