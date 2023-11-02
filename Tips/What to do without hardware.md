It seems you have a solid plan laid out for your project. Since you mentioned that you don't have the hardware yet, you can still make significant progress on the other parts of your project. Here's a suggested approach:

1. **Mock Data for Development**: Even if you don't have the hardware, you can still create mock data to simulate what the hardware would produce. This way, you can build and test your backend and frontend as if you were getting real data. 
    - For example, you can generate random air quality readings in the expected range and use these readings as a placeholder until you get the real data from your sensors.
  
2. **Develop the Website**:
    - **Frontend**: Continue with the design and development of your website. With mock data, you can visualize how the data will be displayed and how users can interact with it.
    - **Backend**: Develop your Flask app, set up SQLite, and create endpoints that the frontend can interact with. Use the mock data as placeholder data.

3. **AI Model Development**:
    - **Data Gathering**: Use public air quality datasets as a starting point. This can serve as a basis for training your model before you have access to your own data.
    - **Model Development**: As you mentioned, starting with simpler models like linear regression is a good approach. Once you have a basic model working, you can experiment with more complex models or fine-tune your current model.
    - **Integration with Flask**: With a trained model, you can then integrate it with Flask as you've outlined.

4. **Plan the Hardware Integration**: Even if you don't have the hardware, you can still:
    - Write pseudocode or actual code (for the Arduino or Raspberry Pi) that you plan to use once you have the hardware.
    - Plan out how you will connect everything. Study datasheets, and gather information on how to set up and read from the sensors.

5. **Documentation & Testing**: While waiting for the hardware, it's a good opportunity to write documentation for what you've developed so far. It's also a perfect time to test your frontend and backend thoroughly using the mock data.

6. **Research & Optimization**:
    - Look into ways to optimize your website for better performance and user experience.
    - Research more about air quality prediction, perhaps there are other factors or models you might want to consider for better accuracy.

7. **Deployment**: As you mentioned, if you aim to make it public, you can start looking into deployment options. Get familiar with platforms like Heroku or PythonAnywhere, as there might be specific requirements or configurations needed for deployment.

Finally, once you get your hardware:

1. **Hardware Integration**: 
    - Setup the hardware, test the sensors, and ensure they're working correctly.
    - Integrate the hardware with your Flask backend, replacing the mock data with real-time data from the sensors.

2. **Final Testing**: 
    - Ensure the entire system works as expected from data collection, processing, prediction, and display.

Remember, every project will have its hiccups and challenges. Embrace them as learning opportunities. Given the thorough plan you have and by following the above suggestions, you'll be in a strong position to deliver a successful project.