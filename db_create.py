from project.ext import db
from project.models import Recipe



recipe1 = Recipe('Slow-Cooker Tacos', 'Delicious ground beef that has been simmering in taco seasoning and sauce.  '
                                      'Perfect with hard-shelled tortillas!')
recipe2 = Recipe('Hamburgers', 'Classic dish elevated with pretzel buns.')
recipe3 = Recipe('Mediterranean Chicken', 'Grilled chicken served with pitas, hummus, and sauted vegetables.')

db.session.add(recipe1)
db.session.add(recipe2)
db.session.add(recipe3)

db.create_all()
db.session.commit()
