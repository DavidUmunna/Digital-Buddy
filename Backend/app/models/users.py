from tortoise import Tortoise, fields, models, run_async

class User(models.Model):
    user_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
    password_hash=fields.CharField(max_length=128)

async def run():
    await Tortoise.init(
        db_url="postgres://username:password@localhost:5432/mydatabase",
        modules={"models": ["__main__"]}
    )
    await Tortoise.generate_schemas()
    await User.create(name="Chima", email="chima@example.com")
    user = await User.get(name="Chima")
    print(user.email)
    await Tortoise.close_connections()

run_async(run())
