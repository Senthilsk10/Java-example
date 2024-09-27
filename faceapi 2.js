const imageUpload = document.getElementById('imageUpload')
const message = document.getElementById('message');
Promise.all([
  faceapi.nets.faceRecognitionNet.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/'),
  faceapi.nets.faceLandmark68Net.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/'),
  faceapi.nets.ssdMobilenetv1.loadFromUri('https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/models/')
]).then(start)

async function start() {
    const labeledFaceDescriptors = await loadLabeledImages()
    const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6)
    let image

    message.innerText = "Model loaded now you can start upload photos";

    imageUpload.addEventListener('change', async () => {
        if (image) image.remove()
        image = await faceapi.bufferToImage(imageUpload.files[0])
        
        const detections = await faceapi.detectAllFaces(image).withFaceLandmarks().withFaceDescriptors()
        const resizedDetections = faceapi.resizeResults(detections, image)
        const results = resizedDetections.map(d => faceMatcher.findBestMatch(d.descriptor))
        const queryParams = getQueryParams(queryString);
        const key = queryParams['key'];
        postData(results, key);

        // Display label results to the user
        const resultLabels = results.map(result => result.label);
        message.innerText = "Labels Detected: " + resultLabels.join(', ');
    })
}


function loadLabeledImages() {

  const labels = ['2238010017','2238010042','2238010058','2238010080','2238010007','22380006']
  return Promise.all(
    labels.map(async label => {
      const descriptions = []
      for (let i = 1; i <= 2; i++) {
        
        const img = await faceapi.fetchImage(`https://raw.githubusercontent.com/Senthilsk10/face-api-web/main/labeled_images/${label}/${i}.jpeg`)
        const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
        descriptions.push(detections.descriptor)
      }

      return new faceapi.LabeledFaceDescriptors(label, descriptions)
    })
  )
}

// Get the full query string from the URL
const queryString = window.location.search;

// Use a function to parse the query string into an object
const getQueryParams = (queryString) => {
  const params = {};
  const searchParams = new URLSearchParams(queryString);

  for (const [key, value] of searchParams.entries()) {
    params[key] = value;
  }

  return params;
};


function postData(results, key) {
    const currentURL = window.location.href;
    const domain = new URL(currentURL).hostname;
    const path = '/staffs/get_result/'; // Specify the path
    const url = '//' + domain + path; // Construct the complete URL using the domain and path
    const labels = results.map(result => result.label); // Extract labels from results
    console.log(labels);
    $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "key": key, "labels": labels }), // Include key and labels in the JSON payload
        success: function(response) {
            console.log('Success:', response);
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
}





