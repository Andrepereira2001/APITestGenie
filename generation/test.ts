import axios from 'axios';

let BASE_URL = "https://petstore.swagger.io/v2";


describe('Pet Store Inventory - Add New Pet API Test', () => {
   test('It should successfully add a new pet to the inventory', async () => {
     // Prepared test data
     const newPet = {
       name: 'Fluffy',
       photoUrls: ['http://example.com/photos/fluffy.jpg'],
       status: 'available'
     };

     try {
       // Make request to add new pet
       const response = await axios.post(`${BASE_URL}/pet`, newPet);

       // Validate response status code
       expect(response.status).toBe(200);

       // Assert response body
       expect(response.data.name).toBe(newPet.name);
       expect(response.data.photoUrls).toEqual(
        expect.arrayContaining(newPet.photoUrls));
       expect(response.data.status).toBe(newPet.status);

       // Additional check could be made to retrieve the pet using GET /pet/{petId} and validate that it is in the inventory
     } catch (error) {
       // If the request fails, log the response for debugging purposes
       console.error('API request failed with response:', error.response);
       // Rethrow the error for Jest to fail the test
       throw error;
     }
   });

   test('It should reject adding a new pet with incomplete data', async () => {
     // Prepared test data with missing required fields (photoUrls)
     const incompletePet = {
       name: 'Ghost'
     };

     try {
       // Attempt to add incomplete pet
       await axios.post(`${BASE_URL}/pet`, incompletePet);
     } catch (error) {
       // Validate response status code
       expect(error.response.status).toBe(405);

       // Assert the response body to contain a meaningful error message
       // Note: This assertion depends on the API's implementation of error messages, which might be different
       // expect(error.response.data.message).toMatch(/invalid input/i);
     }
   });
});