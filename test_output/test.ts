import axios from 'axios';

describe('Add a New Pet to the Store Inventory', () => {
  test('Successfully add a new pet', async () => {
    const url = 'https://petstore.swagger.io/v2/pet';
    // Prepared test data
    const newPet = {
      id: 12345678,
      name: 'Fluffy',
      photoUrls: ['https://example.com/photo1.jpg'],
      category: { id: 1, name: 'Dogs' },
      tags: [{ id: 1, name: 'friendly' }],
      status: 'available',
    };

    // Make request with generated data
    const response = await axios.post(url, newPet);

    // Validate response of request
    expect(response.status).toBe(200);
    expect(response.data).toHaveProperty('id', newPet.id);
    expect(response.data).toHaveProperty('name', newPet.name);
    expect(response.data).toHaveProperty('status', newPet.status);
  });

  test('Fail to add a pet with invalid data', async () => {
    const url = 'https://petstore.swagger.io/v2/pet';
    // Prepared incorrect test data (missing required 'name' field)
    const invalidPet = {
      id: 12345679,
      photoUrls: ['https://example.com/photo2.jpg']
    };

    try {
      // Attempt to make a request with invalid data
      await axios.post(url, invalidPet);
    } catch (error) {
      // Validate response for invalid input
      expect(error.response.status).toBe(405);
    }
  });
});