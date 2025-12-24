use clap::{Parser, Subcommand};
use std::process::Command;
use anyhow::{Result, Context};

#[derive(Parser)]
#[command(name = "garmin-coach")]
#[command(about = "A personal coach for Garmin devices", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Retrieve data from Garmin Connect
    FetchData {
        /// Type of data to fetch (activities, health, stats)
        #[arg(short, long, default_value = "activities")]
        data_type: String,
    },
    /// Get AI coaching feedback
    Coaching {
        /// Type of coaching (activity, health, plan)
        #[arg(short, long, default_value = "activity")]
        coaching_type: String,
    },
    /// Run example scripts
    Example {
        /// Which example to run (data, ai)
        #[arg(short, long, default_value = "data")]
        example_type: String,
    },
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match &cli.command {
        Commands::FetchData { data_type } => {
            println!("Fetching {} data from Garmin Connect...", data_type);
            fetch_garmin_data(data_type)?;
        }
        Commands::Coaching { coaching_type } => {
            println!("Getting {} coaching feedback...", coaching_type);
            get_ai_coaching(coaching_type)?;
        }
        Commands::Example { example_type } => {
            println!("Running {} example...", example_type);
            run_example(example_type)?;
        }
    }

    Ok(())
}

fn fetch_garmin_data(_data_type: &str) -> Result<()> {
    println!("\n📊 Fetching Garmin data using Python client...\n");
    
    let output = Command::new("python3")
        .arg("python_client/example.py")
        .output()
        .context("Failed to execute Python script. Make sure Python 3 is installed.")?;

    if output.status.success() {
        println!("{}", String::from_utf8_lossy(&output.stdout));
        println!("✅ Data fetched successfully!");
    } else {
        eprintln!("❌ Error fetching data:");
        eprintln!("{}", String::from_utf8_lossy(&output.stderr));
    }

    Ok(())
}

fn get_ai_coaching(_coaching_type: &str) -> Result<()> {
    println!("\n🤖 Getting AI coaching feedback...\n");
    
    let output = Command::new("python3")
        .arg("python_client/ai_example.py")
        .output()
        .context("Failed to execute AI coaching script. Make sure Python 3 is installed.")?;

    if output.status.success() {
        println!("{}", String::from_utf8_lossy(&output.stdout));
        println!("✅ Coaching feedback received!");
    } else {
        eprintln!("❌ Error getting coaching:");
        eprintln!("{}", String::from_utf8_lossy(&output.stderr));
    }

    Ok(())
}

fn run_example(example_type: &str) -> Result<()> {
    let script = match example_type {
        "data" => "python_client/example.py",
        "ai" => "python_client/ai_example.py",
        _ => {
            eprintln!("Unknown example type. Use 'data' or 'ai'");
            return Ok(());
        }
    };

    println!("\n🚀 Running {} example...\n", example_type);
    
    let output = Command::new("python3")
        .arg(script)
        .output()
        .context("Failed to execute example script. Make sure Python 3 is installed.")?;

    if output.status.success() {
        println!("{}", String::from_utf8_lossy(&output.stdout));
    } else {
        eprintln!("❌ Error running example:");
        eprintln!("{}", String::from_utf8_lossy(&output.stderr));
    }

    Ok(())
}
