<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, Sparkles, Brain, Search, Cpu, Mail, MessageSquare, Award } from "@lucide/svelte";
</script>

<div class="min-h-screen bg-background text-foreground transition-colors duration-300 relative overflow-hidden">
	<!-- Ambient glow grids -->
	<div class="absolute inset-0 -z-10 bg-[linear-gradient(to_right,#8080800a_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>

	<!-- Navigation Bar -->
	<Navbar />

	<main class="py-16 md:py-24">
		<Container>
			<!-- Back Navigation -->
			<div class="mb-8">
				<a
					href="/"
					class="inline-flex items-center gap-2 rounded-lg border border-border bg-card px-4 py-2 text-sm font-semibold text-muted-foreground hover:text-foreground transition-all hover:border-[#408175]/30 shadow-sm"
				>
					<ArrowLeft class="h-4 w-4 text-[#408175]" />
					<span>Back to Homepage</span>
				</a>
			</div>

			<!-- Hero / Intro -->
			<div class="flex flex-col items-center text-center max-w-3xl mx-auto space-y-6 mb-16">
				<div class="inline-flex items-center gap-1.5 rounded-full border border-[#408175]/30 bg-[#2E4540]/25 px-3.5 py-1 text-xs font-semibold text-[#408175]">
					<Sparkles class="h-3.5 w-3.5" />
					<span>Explore Our Features</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					Powerful AI Tools for <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Job Seekers</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					ReadyHire uses advanced AI analysis to transform your resume, boost keyword alignment, and prepare you for interviews.
				</p>
			</div>

			<!-- Features Grid -->
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8 max-w-6xl mx-auto">
				<!-- Card 1: AI Resume Analysis -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<Brain class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">AI Resume Analysis</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Inspects your resume's structure, layout, and content quality using advanced parsing intelligence.
						</p>
					</div>
				</div>

				<!-- Card 2: ATS Keyword Matching -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<Search class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">ATS Keyword Matching</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Extracts key terms from the job post and checks your resume alignment to help bypass tracking filters.
						</p>
					</div>
				</div>

				<!-- Card 3: Resume Improvements -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<Cpu class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Resume Improvements</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Provides line-by-line rewrite suggestions to highlight achievements and improve readability.
						</p>
					</div>
				</div>

				<!-- Card 4: Cover Letter Generation -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<Mail class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Cover Letter Generation</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Drafts a custom, high-impact cover letter tailored directly to your resume and the target role details.
						</p>
					</div>
				</div>

				<!-- Card 5: Interview Preparation -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<MessageSquare class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Interview Preparation</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Compiles critical behavior and technical mock questions matching your profile and job constraints.
						</p>
					</div>
				</div>

				<!-- Card 6: Application Readiness Score -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md hover:border-[#408175]/30 transition-all duration-300 group shadow-sm flex flex-col justify-between">
					<div>
						<div class="flex h-12 w-12 items-center justify-center rounded-xl bg-[#2E4540]/10 text-[#408175] group-hover:bg-[#2E4540] group-hover:text-white transition-colors duration-300 mb-4">
							<Award class="h-6 w-6" />
						</div>
						<h3 class="font-bold text-lg text-foreground mb-2">Application Readiness Score</h3>
						<p class="text-sm text-muted-foreground leading-relaxed">
							Computes a single readiness percentage showing how well your overall profile aligns with requirements.
						</p>
					</div>
				</div>
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
