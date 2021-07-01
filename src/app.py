import asyncio
from ombori.grid import Module


async def main():
    module = Module()
    await module.connect()

    # Example of receiving initial setting value
    print('Settings', module.settings)

    # Example of receiving setting update
    def settings_handler(settings):
        print('settings updated', settings)
    module.on_settings(settings_handler)

    # Example of a module method
    def on_hello(params):
        print("hello method invoked", params)
        return 123
    module.on_method('hello', on_hello)

    # Example of receiving a message
    def event_handler(params, type):
        print(f"{type} {params}", flush=True)
    module.subscribe('Test.Event', event_handler)

    # Example of broadcasting a message
    async def send_events():
        id = 0
        while True:
            await asyncio.sleep(1)
            module.publish("Test.Event", {"Some": "Data", "SomeId": id})
            id += 1
    asyncio.create_task(send_events())

    # Wait forever after the module is started
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
