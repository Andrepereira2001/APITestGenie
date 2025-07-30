import axios from 'axios';

describe('Adding a New Pet to the Store', () => {
  const baseUrl = 'https://petstore.swagger.io/v2';
  let createdPetId;

  test('should create a unique pet', async () => {
    const newPet = {
      name: 'Fluffy',
      photoUrls: ['http://example.com/photo1'],
      category: { id: 1, name: 'Dogs' },
      tags: [{ id: 1, name: 'Friendly' }],
      status: 'available'
    };

    const response = await axios.post(`${baseUrl}/pet`, newPet, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    // Assuming the response contains the created Pet object
    expect(response.status).toBe(200);
    expect(response.data).toHaveProperty('id');
    createdPetId = response.data.id; // Store the ID for further use
    expect(response.data.name).toBe('Fluffy');
  });

  test('should retrieve the created pet by ID', async () => {
    if (!createdPetId) {
      throw new Error('Failed to store the created pet ID');
    }

    const response = await axios.get(`${baseUrl}/pet/${createdPetId}`, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    expect(response.status).toBe(200);
    expect(response.data.id).toBe(createdPetId);
    expect(response.data.name).toBe('Fluffy');
  });
});