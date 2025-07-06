import gradio as gr
from backend import generate_letter
import os

with gr.Blocks(
    title = "AI Cover Letter Studio",
    theme = gr.themes.Soft(primary_hue = "indigo"),
    css = '''
        body, .dark body {
            background: #0f172a;
            color: #f1f5f9;
        }
        #hero {
            font-size: 2rem;
            font-weight: bold;
            color: #e2e8f0;
            text-align: center;
        }
        #description {
            font-size: 1.2rem;
            margin-bottom: 1.2rem;
            color: #e2e8f0;
            text-align: center;
        }
        .gr-button-primary {
            background: linear-gradient(90deg, #6366F1, #4F46E5);
            border: none;
            color: #fff;
        }
        footer {
            display: none !important;
        }
        #main-row > div {
            height: 100%;
        }
        #credit {
            text-align: center;
            margin-top: 1.2rem;
            font-size: 0.9rem;
        }
        :root {
            --primary: #6366F1;
        }
        .gr-button-primary {
            background: var(--primary);
            border: none;
            color: #fff;
        }
    ''',
) as demo:
    
    demo.load(
        js = '''
            () => {
                document.body.classList.add('dark');
            }
        '''
    )

    gr.HTML(
        '''
            <div id='hero'>
                <strong>
                    AI Cover Letter Studio
                </strong>
            </div>
            <div id='description'>
                Generate a polished job-specific cover letter in seconds.
            </div>
            <div></div>
        '''
    )

    with gr.Row(elem_id = "main-row"):
        with gr.Column(scale=5):
            name = gr.Textbox(
                label = "Your Name",
                placeholder = "Naincy Jain"
            )
            job_role = gr.Textbox(
                label = "Job Title",
                placeholder = "Software Developer Intern"
            )
            company = gr.Textbox(
                label = "Company",
                placeholder = "Google"
            )
            education = gr.Textbox(
                label = "Education",
                placeholder = "Pursuing BTech in Computer Science"
            )
            skills = gr.Textbox(
                label = "Key Skills / Tech Stack",
                placeholder = "Python, SQL, Leadership, CPP, Full Stack Web Development"
            )
            highlights = gr.Textbox(
                label = "Career Highlights",
                placeholder = "Led a Team of 50+ Members in College Chapter, Program Representative for CSE Branch, Merit Scholarship"
            )
            tone = gr.Dropdown(
                ["Formal", "Friendly", "Confident", "Persuasive"],
                value = "Formal",
                label = "Tone"
            )
            words = gr.Slider(
                75, 300,
                value = 150,
                step = 25,
                label = "Approx Word Count"
            )
            generate_btn = gr.Button(
                "Generate Cover Letter",
                variant = "primary",
                interactive = False
            )
        
        with gr.Column(scale = 7):
            output_text = gr.Textbox(
                label = "Cover Letter",
                lines = 35,
                show_copy_button = True,
                interactive = True
            )
            with gr.Row():
                download_btn = gr.DownloadButton(
                    label = "Download Cover Letter",
                    variant = "primary",
                    interactive = False
                )

    def should_enable_generate(name, job_role, company, education, skills, highlights):
        fields = [name, job_role, company, education, skills, highlights]
        filled_count = sum(1 for f in fields if f.strip())
        return gr.update(interactive = (filled_count >= 3))

    inputs = [name, job_role, company, education, skills, highlights]
    for inp in inputs:
        inp.change(
            fn = should_enable_generate,
            inputs = inputs,
            outputs = generate_btn,
            queue = False,
            show_progress = False
        )

    def generate_and_prepare(name, job_role, company, education, skills, highlights, tone, words):
        fields = [name, job_role, company, education, skills, highlights]
        if sum(1 for f in fields if f.strip()) < 3:
            return "⚠️ Enter few details atleast before generating your cover letter",
        gr.update(visible = False)
        letter, pdf_path = generate_letter(name, job_role, company, education, skills, highlights, tone, words)
        return letter, gr.update(
            value = pdf_path,
            interactive = True
        )

    generate_btn.click(
        fn = generate_and_prepare,
        inputs = [name, job_role, company, education, skills, highlights, tone, words],
        outputs = [output_text, download_btn]
    )

    gr.HTML(
        '''
            <div id='credit'>
                Made with &hearts; by Naincy and Aarjav Jain
            </div>
        '''
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    if "PORT" in os.environ:
        demo.launch(server_name="0.0.0.0", server_port=port)
    else:
        demo.launch(server_name="127.0.0.1", server_port=port)