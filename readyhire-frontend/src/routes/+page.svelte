<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import UploadCard from "$lib/components/upload/UploadCard.svelte";
	
	// Report & Analysis components
	import MatchScore from "$lib/components/analysis/MatchScore.svelte";
	import ATSKeywords from "$lib/components/analysis/ATSKeywords.svelte";
	import MissingSkills from "$lib/components/analysis/MissingSkills.svelte";
	import SkillsCard from "$lib/components/analysis/SkillsCard.svelte";
	import ChecklistCard from "$lib/components/report/ChecklistCard.svelte";
	import ResumeImprovements from "$lib/components/report/ResumeImprovements.svelte";
	import InterviewCard from "$lib/components/report/InterviewCard.svelte";
	import CoverLetterCard from "$lib/components/report/CoverLetterCard.svelte";
	import DownloadReport from "$lib/components/report/DownloadReport.svelte";

	import { Sparkles, ArrowRight, Loader2, RefreshCw, FileText, CheckCircle2, AlertCircle, Info } from "@lucide/svelte";
	import { fade, slide } from "svelte/transition";
	import { onMount } from "svelte";
	import { analyzeResume } from "$lib/api/api.js";

	// Page state
	let uploadedFile = $state(null);
	let jobDescription = $state("");
	let isAnalyzing = $state(false);
	let analysisCompleted = $state(false);
	let analysisProgress = $state(0);
	let currentStepMessage = $state("");
	let error = $state(null);
	let reportData = $state(null);

	// Character and word counters
	const wordCount = $derived(jobDescription ? jobDescription.trim().split(/\s+/).filter(Boolean).length : 0);

	// Derived lists for keywords component
	const matchingKeywords = $derived(reportData ? reportData.ats_keywords.filter(k => k.status === 'matched').map(k => k.keyword) : []);
	const missingKeywords = $derived(reportData ? reportData.ats_keywords.filter(k => k.status === 'missing').map(k => k.keyword) : []);
	const keywordPercentage = $derived(reportData ? Math.round((matchingKeywords.length / (reportData.ats_keywords.length || 1)) * 100) + "%" : "");

	// Steps for loading animation
	const loadingSteps = [
		{ min: 0, max: 25, message: "Parsing uploaded resume structure..." },
		{ min: 25, max: 50, message: "Extracting work experience & technical skills..." },
		{ min: 50, max: 75, message: "Cross-referencing keywords with job requirements..." },
		{ min: 75, max: 100, message: "Calculating compatibility scores & preparing recommendations..." }
	];

	async function loadSampleData() {
		try {
			const response = await fetch("/pritesh_frontend_engineer_resume.docx");
			if (!response.ok) throw new Error("Failed to fetch sample resume docx");
			const blob = await response.blob();
			uploadedFile = new File([blob], "pritesh_frontend_engineer_resume.docx", {
				type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
				lastModified: new Date().getTime()
			});
		} catch (e) {
			console.error("Error loading sample data:", e);
			// Fallback to mock file object if fetch fails
			const mockBlob = new Blob(["Pritesh Resume Details"], { type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document" });
			uploadedFile = new File([mockBlob], "pritesh_frontend_engineer_resume.docx", {
				type: "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
				lastModified: new Date().getTime()
			});
		}

		jobDescription = `We are looking for a Frontend Engineer with strong experience in Svelte or React, JavaScript, and Tailwind CSS.

Key requirements:
- Build highly interactive client-side web applications using Svelte/SvelteKit
- Experience with utility-first CSS frameworks like Tailwind CSS
- Proficiency with modern web tooling (Vite, Git, ESLint)
- Knowledge of TypeScript and GraphQL is a strong plus
- Familiarity with CI/CD pipelines, Jest/Vitest for unit testing, and Agile/Scrum methodologies`;
	}

	async function runAnalysis() {
		if (!uploadedFile || !jobDescription.trim()) return;

		isAnalyzing = true;
		analysisCompleted = false;
		error = null;
		analysisProgress = 0;
		currentStepMessage = loadingSteps[0].message;

		// Timer to simulate progress up to 92%
		const maxSimulatedProgress = 92;
		const duration = 5000; // 5 seconds
		const intervalTime = 50;
		const totalSteps = duration / intervalTime;
		const stepIncrement = maxSimulatedProgress / totalSteps;

		const timer = setInterval(() => {
			if (analysisProgress < maxSimulatedProgress) {
				analysisProgress += stepIncrement;
				// Update progress message based on progress bracket
				const activeStep = loadingSteps.find(step => analysisProgress >= step.min && analysisProgress < step.max);
				if (activeStep) {
					currentStepMessage = activeStep.message;
				}
			}
		}, intervalTime);

		try {
			const result = await analyzeResume(uploadedFile, jobDescription);
			
			// Clear simulation timer
			clearInterval(timer);
			
			// Fill progress to 100% smoothly
			analysisProgress = 100;
			currentStepMessage = "Analysis complete!";
			
			// Let user see 100% progress for a brief moment, then display report
			setTimeout(() => {
				reportData = result;
				isAnalyzing = false;
				analysisCompleted = true;
				
				// Scroll to report view after rendering
				setTimeout(() => {
					document.getElementById("report-results")?.scrollIntoView({ behavior: "smooth" });
				}, 150);
			}, 300);

		} catch (err) {
			clearInterval(timer);
			isAnalyzing = false;
			analysisCompleted = false;
			error = err.message || "An unexpected error occurred.";
		}
	}

	function resetAnalyzer() {
		uploadedFile = null;
		jobDescription = "";
		reportData = null;
		error = null;
		analysisCompleted = false;
		analysisProgress = 0;
		currentStepMessage = "";
		window.scrollTo({ top: 0, behavior: "smooth" });
	}
</script>

<div class="min-h-screen bg-background text-foreground transition-colors duration-300 relative overflow-hidden">
	<!-- Ambient glow grids -->
	<div class="absolute inset-0 -z-10 bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>

	<!-- Navigation Bar -->
	<Navbar />

	<!-- Hero Section -->
	<header class="py-16 md:py-24">
		<Container>
			<div class="flex flex-col items-center text-center max-w-3xl mx-auto space-y-6">
				<!-- Tagline Badge -->
				<div class="inline-flex items-center gap-1.5 rounded-full border border-[#408175]/30 bg-[#2E4540]/25 px-3.5 py-1 text-xs font-semibold text-[#408175]">
					<Sparkles class="h-3.5 w-3.5" />
					<span>AI-Powered Recruitment Analytics</span>
				</div>

				<h1 class="text-4xl md:text-6xl font-extrabold tracking-tight leading-none">
					Turn Every Job Application into <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Your Best One</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					Upload your resume, paste the target job description, and get instant feedback with actionable optimizations, keywords, and interview preparation.
				</p>

				<!-- Mock CTA / Demo trigger -->
				{#if !uploadedFile && !jobDescription}
					<button
						onclick={loadSampleData}
						class="inline-flex items-center gap-2 rounded-xl bg-secondary hover:bg-muted border border-border px-5 py-2.5 text-sm font-semibold text-foreground shadow transition-all active:scale-[0.98]"
					>
						Try with Sample Data
						<ArrowRight class="h-4 w-4" />
					</button>
				{/if}
			</div>
		</Container>
	</header>

	<!-- Main Analyzer Area -->
	<main id="analyzer" class="pb-24">
		<Container>
			<!-- Analyzer Input Panel -->
			{#if !isAnalyzing && !analysisCompleted && !error}
				<div
					in:fade={{ duration: 300 }}
					class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start rounded-3xl border border-border/60 bg-card/60 backdrop-blur-md p-6 md:p-8 shadow-xl relative"
				>

					<!-- Upload Section -->
					<div class="lg:col-span-6 space-y-4">
						<div class="flex items-center justify-between">
							<h2 class="font-bold text-lg text-foreground tracking-tight flex items-center gap-2">
								1. Upload Resume
							</h2>
							{#if uploadedFile}
								<span class="text-xs text-emerald-500 flex items-center gap-1">
									<CheckCircle2 class="h-3.5 w-3.5" /> File loaded
								</span>
							{/if}
						</div>
						
						<!-- Upload Card binding file -->
						<UploadCard
							bind:file={uploadedFile}
							onRemove={() => (uploadedFile = null)}
						/>

						<div class="rounded-xl border border-border bg-muted/20 p-4 text-xs text-muted-foreground space-y-2">
							<p class="font-semibold text-foreground flex items-center gap-1.5">
								<Info class="h-3.5 w-3.5 text-[#408175]" />
								Why Upload a Resume?
							</p>
							<p class="leading-relaxed">
								Modern ATS platforms automatically scan your resume for keyword matches, experience timeline formatting, and structural structure.
							</p>
						</div>
					</div>

					<!-- Job Description Section -->
					<div class="lg:col-span-6 space-y-4">
						<div class="flex items-center justify-between">
							<h2 class="font-bold text-lg text-foreground tracking-tight">
								2. Paste Job Description
							</h2>
							<span class="text-xs text-muted-foreground">
								{wordCount} words
							</span>
						</div>

						<!-- Textarea wrapper -->
						<div class="relative rounded-2xl border border-border bg-card focus-within:border-[#408175] focus-within:ring-2 focus-within:ring-[#408175]/20 transition-all duration-300 overflow-hidden">
							<textarea
								bind:value={jobDescription}
								placeholder="Paste the key responsibilities, requirements, and tech stack details of the job listing here..."
								class="w-full h-[220px] p-4 bg-transparent border-0 outline-none text-sm resize-none leading-relaxed placeholder:text-muted-foreground/60 select-text"
							></textarea>
						</div>

						<div class="flex items-center justify-between gap-4">
							<span class="text-xs text-muted-foreground">
								Tip: Include both qualifications and tech stack requirements.
							</span>
							{#if jobDescription}
								<button
									onclick={() => (jobDescription = "")}
									class="text-xs text-muted-foreground hover:text-foreground transition-colors font-medium"
								>
									Clear Text
								</button>
							{/if}
						</div>
					</div>

					<!-- CTA Submit Panel -->
					<div class="lg:col-span-12 border-t border-border/40 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4">
						<div class="text-xs text-muted-foreground text-center sm:text-left">
							{#if !uploadedFile && !jobDescription}
								Please upload a resume and paste the job description to run analysis.
							{:else}
								Ready to scan resume for keyword alignment and formatting guidelines.
							{/if}
						</div>

						<div class="flex items-center gap-3 w-full sm:w-auto">
							<button
								onclick={runAnalysis}
								disabled={!uploadedFile || !jobDescription.trim() || isAnalyzing}
								class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#2E4540] hover:bg-[#408175] disabled:bg-muted disabled:text-muted-foreground disabled:border-border font-semibold text-white px-6 shadow-sm shadow-[#2E4540]/30 disabled:shadow-none transition-all active:scale-[0.98] w-full sm:w-auto shrink-0 select-none cursor-pointer disabled:cursor-not-allowed"
							>
								<Sparkles class="h-4.5 w-4.5" />
								<span>Analyze Application</span>
							</button>
						</div>
					</div>
				</div>
			{/if}

			<!-- Error State -->
			{#if error}
				<div
					in:fade={{ duration: 200 }}
					class="flex flex-col items-center justify-center min-h-[350px] rounded-3xl border border-[#D95C5C]/20 bg-[#D95C5C]/5 backdrop-blur-md p-8 md:p-12 text-center max-w-xl mx-auto shadow-xl space-y-6"
				>
					<div class="relative flex items-center justify-center">
						<div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-[#D95C5C]/15 text-[#D95C5C]">
							<AlertCircle class="h-8 w-8" />
						</div>
					</div>

					<div class="space-y-2">
						<h3 class="font-bold text-xl text-foreground">Analysis Failed</h3>
						<p class="text-sm text-muted-foreground max-w-md mx-auto leading-relaxed">
							{error}
						</p>
					</div>

					<div class="flex flex-col sm:flex-row items-center justify-center gap-3 w-full pt-2">
						<button
							onclick={runAnalysis}
							class="inline-flex h-11 items-center justify-center gap-2 rounded-xl bg-[#2E4540] hover:bg-[#408175] font-semibold text-white px-6 shadow-sm shadow-[#2E4540]/30 transition-all active:scale-[0.98] w-full sm:w-auto cursor-pointer"
						>
							<RefreshCw class="h-4 w-4" />
							<span>Retry Analysis</span>
						</button>
						<button
							onclick={() => { error = null; isAnalyzing = false; analysisCompleted = false; }}
							class="inline-flex h-11 items-center justify-center gap-2 rounded-xl border border-border bg-background px-6 text-sm font-semibold text-foreground hover:bg-muted transition-all active:scale-[0.98] w-full sm:w-auto cursor-pointer"
						>
							<span>Edit Inputs</span>
						</button>
					</div>
				</div>
			{/if}

			<!-- Loading State -->
			{#if isAnalyzing}
				<div
					in:fade={{ duration: 200 }}
					class="flex flex-col items-center justify-center min-h-[400px] rounded-3xl border border-border bg-card/60 backdrop-blur-md p-8 md:p-12 text-center max-w-xl mx-auto shadow-xl space-y-6"
				>
					<div class="relative flex items-center justify-center">
						<Loader2 class="h-16 w-16 text-[#408175] animate-spin" />
					</div>

					<div class="space-y-2">
						<h3 class="font-bold text-xl text-foreground">Analyzing Application</h3>
						<p class="text-sm text-muted-foreground max-w-sm mx-auto animate-pulse">
							{currentStepMessage}
						</p>
					</div>

					<!-- Progress bar -->
					<div class="w-full max-w-xs space-y-1.5">
						<div class="h-2 w-full rounded-full bg-muted overflow-hidden">
							<div
								class="h-full bg-gradient-to-r from-[#2E4540] to-[#408175] transition-all duration-150 rounded-full"
								style="width: {analysisProgress}%"
							></div>
						</div>
						<div class="flex justify-between text-xs text-muted-foreground font-medium">
							<span>ATS Scan</span>
							<span>{Math.round(analysisProgress)}%</span>
						</div>
					</div>
				</div>
			{/if}

			<!-- Empty State / Analysis Report -->
			{#if analysisCompleted && reportData}
				<div
					id="report-results"
					in:fade={{ duration: 400 }}
					class="space-y-8"
				>
					<!-- Report Header Info -->
					<div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4 bg-muted/20 border border-border/80 rounded-2xl p-5">
						<div class="flex items-start gap-4">
							<div class="flex h-11 w-11 items-center justify-center rounded-xl bg-[#2E4540]/15 text-[#408175] shrink-0">
								<FileText class="h-5.5 w-5.5" />
							</div>
							<div>
								<h3 class="font-bold text-base text-foreground leading-snug">
									Analysis Report
								</h3>
								<p class="text-xs text-muted-foreground mt-0.5">
									Checked <span class="text-foreground font-semibold">{uploadedFile?.name}</span> against matching requirements.
								</p>
							</div>
						</div>

						<button
							onclick={resetAnalyzer}
							class="inline-flex h-9 items-center justify-center gap-1.5 rounded-lg border border-border bg-background px-3 text-xs font-semibold hover:bg-muted transition-all active:scale-[0.98] self-start md:self-center cursor-pointer"
						>
							<RefreshCw class="h-3.5 w-3.5" />
							<span>Analyze Another Application</span>
						</button>
					</div>

					<!-- Results Grid (Score & Keywords) -->
					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
						<!-- Match Score: Spans 5 columns -->
						<div class="lg:col-span-5 flex flex-col h-full">
							<MatchScore 
								score={reportData.readiness_score} 
								{keywordPercentage} 
							/>
						</div>

						<!-- Keywords: Spans 7 columns -->
						<div class="lg:col-span-7 flex flex-col h-full">
							<ATSKeywords 
								matching={matchingKeywords} 
								missing={missingKeywords} 
							/>
						</div>
					</div>

					<!-- Technical Gaps & Extracted Skills -->
					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
						<div class="lg:col-span-6 flex flex-col h-full">
							<MissingSkills skills={reportData.missing_skills} />
						</div>

						<div class="lg:col-span-6 flex flex-col h-full">
							<SkillsCard categories={reportData.matched_skills} />
						</div>
					</div>

					<!-- Formatting Quality Checklist & Rewrite Recommendations -->
					<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
						<div class="lg:col-span-5 flex flex-col gap-6">
							<ChecklistCard items={reportData.checklist} />
						</div>

						<div class="lg:col-span-7 flex flex-col gap-6">
							<ResumeImprovements improvements={reportData.resume_improvements} />
						</div>
					</div>

					<!-- Interview Prep Questions -->
					<div class="grid grid-cols-1 gap-8">
						<InterviewCard questions={reportData.interview_questions} />
					</div>

					<!-- Tailored Cover Letter -->
					<div class="grid grid-cols-1 gap-8">
						<CoverLetterCard draft={reportData.cover_letter} />
					</div>

					<!-- Download and Save Banner (Temporarily hidden until PDF export is fully implemented) -->
					{#if false}
						<DownloadReport />
					{/if}
				</div>
			{/if}
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>

<style>
	/* Custom accessibility utilities & print stylesheet integration */
	@media print {
		:global(nav), :global(footer), :global(button), :global(#analyzer) {
			display: none !important;
		}
		:global(body) {
			background: white !important;
			color: black !important;
		}
		:global(#report-results) {
			display: block !important;
			margin: 0 !important;
			padding: 0 !important;
		}
	}
</style>
