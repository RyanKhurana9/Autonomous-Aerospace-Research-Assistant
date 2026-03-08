from agent import agent_executor
print(" Aerospace Agent ready! Type 'exit' to quit.\n")
while True:
    user_input=input("You:")
    if user_input.lower() in['quit','exit']:
        print("GoodBye")
        break
    response = agent_executor.invoke({"input": user_input})
    print(f"\nAgent: {response['output']}\n")
        