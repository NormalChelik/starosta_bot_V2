from dataclasses import dataclass


# [Lesson(from_time='09:00', to_time='10:30', title='Начертательная геометрия, инженерная и компьютерная графика', is_verified=True), Lesson(from_time='10:40', to_time='12:10', title='История России', is_verified=False), Lesson(from_time='12:40', to_time='14:10', title='Начертательная геометрия и инженерная и компьютерная графика', is_verified=False), Lesson(from_time='14:20', to_time='15:50', title='История России', is_verified=False)]
@dataclass
class Lesson:
    from_time: str
    to_time: str
    title: str
    is_verified: bool
