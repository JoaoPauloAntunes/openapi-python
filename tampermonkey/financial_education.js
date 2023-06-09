// ==UserScript==
// @name         OpenAI GPT-3: Financial Education
// @version      1
// @description  Generates a blog article using OpenAI's GPT-3 API and prints the response in the console with elapsed time
// @match        *://*/*
// @grant        none
// ==/UserScript==

(async () => {
    'use strict';

    const getAPIKey = async () => {
        // Obter a chave de API
        const res = await fetch("http://127.0.0.1:2334/OPENAI_API_KEY");
        const data = await res.json();
        return data.data.OPENAI_API_KEY;
    }

    const generateResponse = async (apiKey, prompt, model_engine, max_tokens, temperature) => {
        // Gerar resposta do GPT-3
        const response = await fetch(`https://api.openai.com/v1/engines/${model_engine}/completions`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                prompt: prompt,
                max_tokens: max_tokens,
                temperature: temperature
            })
        });
        const data = await response.json();
        return data.choices[0].text;
    }


    // Obter a chave de API
    const apiKey = await getAPIKey();

    // Prompt para gerar o artigo
    const prompt = "escreva um artigo de blog falando sobre educação financeira";
    console.log("prompt: ", prompt);

    // Parâmetros para GPT-3
    const model_engine = "text-davinci-002";
    const max_tokens = 1024;
    const temperature = 0.5;

    const res = await generateResponse(apiKey, prompt, model_engine, max_tokens, temperature);
    console.log(res);
})();
