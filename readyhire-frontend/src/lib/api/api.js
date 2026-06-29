// ReadyHire API Service

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

/**
 * Analyzes a resume file against a job description.
 * 
 * @param {File} resumeFile - PDF or DOCX file object
 * @param {string} jobDescription - Plain text of the job description
 * @returns {Promise<Object>} - The structured analysis report
 */
export async function analyzeResume(resumeFile, jobDescription) {
	if (!resumeFile) {
		throw new Error('Please upload a resume file.');
	}
	if (!jobDescription || !jobDescription.trim()) {
		throw new Error('Please enter a job description.');
	}

	const formData = new FormData();
	formData.append('resume', resumeFile);
	formData.append('job_description', jobDescription);

	try {
		const response = await fetch(`${API_BASE_URL}/analyze`, {
			method: 'POST',
			body: formData,
			// Note: We do NOT set the 'Content-Type' header. 
			// Letting the browser set it automatically ensures the boundary parameter is generated correctly.
		});

		if (!response.ok) {
			let errorMessage = '';
			let errorDetail = null;

			try {
				const errorJson = await response.json();
				errorDetail = errorJson.detail;
			} catch (e) {
				// Response was not JSON
			}

			// Format friendly message based on status code
			switch (response.status) {
				case 400:
					errorMessage = typeof errorDetail === 'string' 
						? errorDetail 
						: 'Invalid input or invalid file format. Please upload a valid PDF or DOCX resume.';
					break;
				case 422:
					errorMessage = typeof errorDetail === 'string'
						? errorDetail
						: Array.isArray(errorDetail)
							? `Validation Error: ${errorDetail.map(err => err.msg || err.loc.join('.')).join(', ')}`
							: 'The analysis model response was in an invalid format. Please try again.';
					break;
				case 503:
					errorMessage = typeof errorDetail === 'string'
						? errorDetail
						: 'The AI analysis service is temporarily busy or unavailable. Please try again in a few moments.';
					break;
				case 500:
					errorMessage = typeof errorDetail === 'string'
						? errorDetail
						: 'An internal server error occurred while parsing or analyzing your resume. Please try again later.';
					break;
				default:
					errorMessage = typeof errorDetail === 'string'
						? errorDetail
						: `Server returned an error (HTTP ${response.status}). Please try again.`;
			}

			const error = new Error(errorMessage);
			error.status = response.status;
			throw error;
		}

		const data = await response.json();
		return data;
	} catch (error) {
		// Network errors / Fetch failures
		if (!error.status) {
			const connectionError = new Error(
				`Failed to connect to the backend server. Please verify that the API is running at ${API_BASE_URL} and your internet connection is active.`
			);
			connectionError.status = 0;
			throw connectionError;
		}
		throw error;
	}
}
