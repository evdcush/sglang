import sglang as sgl


@sgl.function
def few_shot_qa(s, question):
    s += "Please answer this 

runtime = Runtime(model_path="meta-llama/Llama-2-7b-chat-hf")
set_default_backend(runtime)

state = few_shot_qa.run(question="What is the capital of the United States?")



def main():
    pass


if __name__ == "__main__":
    main()
