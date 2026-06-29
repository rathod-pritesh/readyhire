<script>
	import Navbar from "$lib/components/layout/Navbar.svelte";
	import Footer from "$lib/components/layout/Footer.svelte";
	import Container from "$lib/components/layout/Container.svelte";
	import { ArrowLeft, Shield, Upload, Clock, Eye, Trash2, Mail } from "@lucide/svelte";
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
					<Shield class="h-3.5 w-3.5" />
					<span>Privacy First</span>
				</div>

				<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight leading-none">
					Privacy <span class="bg-gradient-to-r from-[#2E4540] to-[#408175] bg-clip-text text-transparent">Policy</span>
				</h1>

				<p class="text-base md:text-lg text-muted-foreground max-w-xl leading-relaxed">
					We keep our privacy policies simple and transparent. No complex legalese or hidden clauses.
				</p>
			</div>

			<!-- Policy Sections Grid -->
			<div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8 max-w-4xl mx-auto">
				<!-- Information Uploaded -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Upload class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Information Uploaded</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						We only access the files and job description texts you explicitly paste or upload to run analysis. We do not access background folders or device files.
					</p>
				</div>

				<!-- Temporary Processing -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Clock class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Temporary Processing</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						Uploaded files are processed in-memory to generate report insights. We do not store your documents permanently on our database servers.
					</p>
				</div>

				<!-- AI Analysis -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Eye class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">AI Analysis</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						Resume content is processed securely using AI APIs to compile feedback. No partner models use your personal content for generic machine learning training.
					</p>
				</div>

				<!-- No Selling of User Data -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Trash2 class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">No Selling of User Data</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						We do not sell, license, rent, or distribute your email addresses, resume contents, or career search histories to recruiters or third-party advertisers.
					</p>
				</div>

				<!-- Contact -->
				<div class="p-6 rounded-2xl border border-border/60 bg-card/60 backdrop-blur-md shadow-sm space-y-3 md:col-span-2">
					<div class="flex h-10 w-10 items-center justify-center rounded-lg bg-[#2E4540]/10 text-[#408175]">
						<Mail class="h-5 w-5" />
					</div>
					<h3 class="font-bold text-lg text-foreground">Contact</h3>
					<p class="text-sm text-muted-foreground leading-relaxed">
						If you have any questions about how we handle your files or want to request complete data clearance, feel free to contact us at <a href="mailto:privacy@readyhire.com" class="text-[#408175] font-semibold hover:underline">privacy@readyhire.com</a>.
					</p>
				</div>
			</div>
		</Container>
	</main>

	<!-- Footer -->
	<Footer />
</div>
